import json
import mock
import pandas as pd
import pytest
from surrogate import surrogate

from wetterdienst.dwd.observations import (
    DWDObservationData,
    DWDObsParameterSet,
    DWDObsTimeResolution,
    DWDObsPeriodType,
)
from wetterdienst.dwd.util import parse_datetime

df_station = pd.DataFrame.from_dict(
    [
        {
            "STATION_ID": 19087,
            "FROM_DATE": parse_datetime("1957-05-01T00:00:00.000Z"),
            "TO_DATE": parse_datetime("1995-11-30T00:00:00.000Z"),
            "STATION_HEIGHT": 645.0,
            "LAT": 48.8049,
            "LON": 13.5528,
            "STATION_NAME": "Freyung vorm Wald",
            "STATE": "Bayern",
            "HAS_FILE": False,
        }
    ]
)

df_data = pd.DataFrame.from_dict(
    [
        {
            "STATION_ID": 1048,
            "PARAMETER": "CLIMATE_SUMMARY",
            "ELEMENT": "TEMPERATURE_AIR_MAX_200",
            "DATE": parse_datetime("2019-12-28T00:00:00.000Z"),
            "VALUE": 1.3,
            "QUALITY": None,
        }
    ]
)


def test_lowercase():

    df = df_data.dwd.lower()

    assert list(df.columns) == [
        "station_id",
        "parameter",
        "element",
        "date",
        "value",
        "quality",
    ]

    assert df.iloc[0]["parameter"] == "climate_summary"
    assert df.iloc[0]["element"] == "temperature_air_max_200"


def test_filter_by_date():

    df = df_data.dwd.filter_by_date("2019-12-28Z", DWDObsTimeResolution.HOURLY)
    assert not df.empty

    df = df_data.dwd.filter_by_date("2019-12-27Z", DWDObsTimeResolution.HOURLY)
    assert df.empty


def test_filter_by_date_interval():

    df = df_data.dwd.filter_by_date(
        "2019-12-27Z/2019-12-29Z", DWDObsTimeResolution.HOURLY
    )
    assert not df.empty

    df = df_data.dwd.filter_by_date("2020Z/2022Z", DWDObsTimeResolution.HOURLY)
    assert df.empty


def test_filter_by_date_monthly():

    result = pd.DataFrame.from_dict(
        [
            {
                "STATION_ID": 1048,
                "PARAMETER": "climate_summary",
                "ELEMENT": "temperature_air_max_200",
                "FROM_DATE": parse_datetime("2019-12-28T00:00:00.000"),
                "TO_DATE": parse_datetime("2020-01-28T00:00:00.000"),
                "VALUE": 1.3,
                "QUALITY": None,
            }
        ]
    )

    df = result.dwd.filter_by_date("2019-12/2020-01", DWDObsTimeResolution.MONTHLY)
    assert not df.empty

    df = result.dwd.filter_by_date("2020/2022", DWDObsTimeResolution.MONTHLY)
    assert df.empty

    df = result.dwd.filter_by_date("2020", DWDObsTimeResolution.MONTHLY)
    assert df.empty


def test_filter_by_date_annual():

    result = pd.DataFrame.from_dict(
        [
            {
                "STATION_ID": 1048,
                "PARAMETER": "climate_summary",
                "ELEMENT": "temperature_air_max_200",
                "FROM_DATE": parse_datetime("2019-01-01T00:00:00.000"),
                "TO_DATE": parse_datetime("2019-12-31T00:00:00.000"),
                "VALUE": 1.3,
                "QUALITY": None,
            }
        ]
    )

    df = result.dwd.filter_by_date("2019-05/2019-09", DWDObsTimeResolution.ANNUAL)
    assert not df.empty

    df = result.dwd.filter_by_date("2020/2022", DWDObsTimeResolution.ANNUAL)
    assert df.empty

    df = result.dwd.filter_by_date("2020", DWDObsTimeResolution.ANNUAL)
    assert df.empty


@pytest.mark.sql
def test_filter_by_sql():

    df = df_data.dwd.lower().io.sql(
        "SELECT * FROM data WHERE element='temperature_air_max_200' AND value < 1.5"
    )
    assert not df.empty

    df = df_data.dwd.lower().io.sql(
        "SELECT * FROM data WHERE element='temperature_air_max_200' AND value > 1.5"
    )
    assert df.empty


def test_format_json():

    output = df_data.dwd.lower().io.format("json")

    response = json.loads(output)
    station_ids = list(set([reading["station_id"] for reading in response]))

    assert 1048 in station_ids


def test_format_geojson():

    output = df_station.dwd.format("geojson")

    response = json.loads(output)

    station_names = [station["properties"]["name"] for station in response["features"]]

    assert "Freyung vorm Wald" in station_names


def test_format_csv():

    output = df_data.dwd.lower().io.format("csv").strip()

    assert "station_id,parameter,element,date,value,quality" in output
    assert (
        "1048,climate_summary,temperature_air_max_200,2019-12-28T00-00-00,1.3,"
        in output
    )


def test_format_unknown():

    with pytest.raises(KeyError):
        df_data.dwd.format("foobar")


def test_request():

    observations = DWDObservationData(
        station_ids=[1048],
        parameters=DWDObsParameterSet.CLIMATE_SUMMARY,
        time_resolution=DWDObsTimeResolution.DAILY,
        period_types=DWDObsPeriodType.RECENT,
    )

    df = observations.collect_safe()
    assert not df.empty


def test_export_sqlite():

    observations = DWDObservationData(
        station_ids=[1048],
        parameters=DWDObsParameterSet.CLIMATE_SUMMARY,
        time_resolution=DWDObsTimeResolution.DAILY,
        period_types=DWDObsPeriodType.RECENT,
    )

    with mock.patch(
        "pandas.DataFrame.to_sql",
    ) as mock_to_sql:

        df = observations.collect_safe()
        df.io.export("sqlite:///test.sqlite?table=testdrive")

        mock_to_sql.assert_called_once_with(
            name="testdrive",
            con="sqlite:///test.sqlite?table=testdrive",
            if_exists="replace",
            index=False,
            method="multi",
            chunksize=5000,
        )


def test_export_crate():

    observations = DWDObservationData(
        station_ids=[1048],
        parameters=DWDObsParameterSet.CLIMATE_SUMMARY,
        time_resolution=DWDObsTimeResolution.DAILY,
        period_types=DWDObsPeriodType.RECENT,
    )

    with mock.patch(
        "pandas.DataFrame.to_sql",
    ) as mock_to_sql:

        df = observations.collect_safe()
        df.io.export("crate://localhost/?database=test&table=testdrive")

        mock_to_sql.assert_called_once_with(
            name="testdrive",
            con="crate://localhost/?database=test&table=testdrive",
            if_exists="replace",
            index=False,
            method="multi",
            chunksize=5000,
        )


@surrogate("duckdb.connect")
def test_export_duckdb():

    observations = DWDObservationData(
        station_ids=[1048],
        parameters=DWDObsParameterSet.CLIMATE_SUMMARY,
        time_resolution=DWDObsTimeResolution.DAILY,
        period_types=DWDObsPeriodType.RECENT,
    )

    mock_connection = mock.MagicMock()
    with mock.patch(
        "duckdb.connect", side_effect=[mock_connection], create=True
    ) as mock_connect:

        df = observations.collect_safe()
        df.io.export("duckdb:///test.duckdb?table=testdrive")

        mock_connect.assert_called_once_with(database="test.duckdb", read_only=False)
        mock_connection.register.assert_called_once()
        mock_connection.execute.assert_called()
        mock_connection.table.assert_called_once_with("testdrive")
        # a.table.to_df.assert_called()
        mock_connection.close.assert_called_once()


@surrogate("influxdb.dataframe_client.DataFrameClient")
def test_export_influxdb():

    observations = DWDObservationData(
        station_ids=[1048],
        parameters=DWDObsParameterSet.CLIMATE_SUMMARY,
        time_resolution=DWDObsTimeResolution.DAILY,
        period_types=DWDObsPeriodType.RECENT,
    )

    mock_client = mock.MagicMock()
    with mock.patch(
        "influxdb.dataframe_client.DataFrameClient",
        side_effect=[mock_client],
        create=True,
    ) as mock_connect:

        df = observations.collect_safe()
        df.dwd.lower().io.export("influxdb://localhost/?database=dwd&table=weather")

        mock_connect.assert_called_once_with(database="dwd")
        mock_client.create_database.assert_called_once_with("dwd")
        mock_client.write_points.assert_called_once()
