from __future__ import annotations

from wetterdienst.core.timeseries.metadata import DATASET_NAME_DEFAULT, build_metadata_model

EcccObservationMetadata = {
    "resolutions": [
        {
            "name": "hourly",
            "name_original": "hourly",
            "periods": ["historical"],
            "date_required": True,
            "datasets": [
                {
                    "name": DATASET_NAME_DEFAULT,
                    "name_original": DATASET_NAME_DEFAULT,
                    "grouped": True,
                    "parameters": [
                        {
                            "name": "temperature_air_mean_2m",
                            "name_original": "temp (°c)",
                            "unit_type": "temperature",
                            "unit": "degree_celsius",
                        },
                        {
                            "name": "quality_temperature_air_mean_2m",
                            "name_original": "temp flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "temperature_dew_point_mean_2m",
                            "name_original": "dew point temp (°c)",
                            "unit_type": "temperature",
                            "unit": "degree_celsius",
                        },
                        {
                            "name": "quality_temperature_dew_point_mean_2m",
                            "name_original": "dew point temp flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "humidity",
                            "name_original": "rel hum (%)",
                            "unit_type": "fraction",
                            "unit": "percent",
                        },
                        {
                            "name": "quality_humidity",
                            "name_original": "rel hum flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "wind_direction",
                            "name_original": "wind dir (10s deg)",
                            "unit_type": "angle",
                            "unit": "degree",
                        },
                        {
                            "name": "quality_wind_direction",
                            "name_original": "wind dir flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "wind_speed",
                            "name_original": "wind spd (km/h)",
                            "unit_type": "speed",
                            "unit": "kilometer_per_hour",
                        },
                        {
                            "name": "quality_wind_speed",
                            "name_original": "wind spd flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "visibility_range",
                            "name_original": "visibility (km)",
                            "unit_type": "length_medium",
                            "unit": "kilometer",
                        },
                        {
                            "name": "quality_visibility_range",
                            "name_original": "visibility flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "pressure_air_site",
                            "name_original": "stn press (kpa)",
                            "unit_type": "pressure",
                            "unit": "kilopascal",
                        },
                        {
                            "name": "quality_pressure_air_site",
                            "name_original": "stn press flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "humidex",
                            "name_original": "hmdx",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "quality_humidex",
                            "name_original": "hmdx flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "wind_gust_max",
                            "name_original": "wind chill",
                            "unit_type": "speed",
                            "unit": "kilometer_per_hour",
                        },
                        {
                            "name": "quality_wind_gust_max",
                            "name_original": "wind chill flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "weather",
                            "name_original": "weather",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                    ],
                }
            ],
        },
        {
            "name": "daily",
            "name_original": "daily",
            "periods": ["historical"],
            "date_required": True,
            "datasets": [
                {
                    "name": DATASET_NAME_DEFAULT,
                    "name_original": DATASET_NAME_DEFAULT,
                    "grouped": True,
                    "parameters": [
                        {
                            "name": "temperature_air_max_2m",
                            "name_original": "max temp (°c)",
                            "unit_type": "temperature",
                            "unit": "degree_celsius",
                        },
                        {
                            "name": "quality_temperature_air_max_2m",
                            "name_original": "max temp flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "temperature_air_min_2m",
                            "name_original": "min temp (°c)",
                            "unit_type": "temperature",
                            "unit": "degree_celsius",
                        },
                        {
                            "name": "quality_temperature_air_min_2m",
                            "name_original": "min temp flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "temperature_air_mean_2m",
                            "name_original": "mean temp (°c)",
                            "unit_type": "temperature",
                            "unit": "degree_celsius",
                        },
                        {
                            "name": "quality_temperature_air_mean_2m",
                            "name_original": "mean temp flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "count_days_heating_degree",
                            "name_original": "heat deg days (°c)",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "quality_count_days_heating_degree",
                            "name_original": "heat deg days flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "count_days_cooling_degree",
                            "name_original": "cool deg days (°c)",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "quality_count_days_cooling_degree",
                            "name_original": "cool deg days flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "precipitation_height_liquid",
                            "name_original": "total rain (mm)",
                            "unit_type": "precipitation",
                            "unit": "millimeter",
                        },
                        {
                            "name": "quality_precipitation_height_liquid",
                            "name_original": "total rain flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "snow_depth_new",
                            "name_original": "total snow (cm)",
                            "unit_type": "length_short",
                            "unit": "centimeter",
                        },
                        {
                            "name": "quality_snow_depth_new",
                            "name_original": "total snow flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "precipitation_height",
                            "name_original": "total precip (mm)",
                            "unit_type": "precipitation",
                            "unit": "millimeter",
                        },
                        {
                            "name": "quality_precipitation_height",
                            "name_original": "total precip flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "snow_depth",
                            "name_original": "snow on grnd (cm)",
                            "unit_type": "length_short",
                            "unit": "centimeter",
                        },
                        {
                            "name": "quality_snow_depth",
                            "name_original": "snow on grnd flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "wind_direction_gust_max",
                            "name_original": "dir of max gust (10s deg)",
                            "unit_type": "angle",
                            "unit": "degree",
                        },
                        {
                            "name": "quality_wind_direction_gust_max",
                            "name_original": "dir of max gust flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "wind_gust_max",
                            "name_original": "spd of max gust (km/h)",
                            "unit_type": "speed",
                            "unit": "kilometer_per_hour",
                        },
                        {
                            "name": "quality_wind_gust_max",
                            "name_original": "spd of max gust flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                    ],
                }
            ],
        },
        {
            "name": "monthly",
            "name_original": "monthly",
            "periods": ["historical"],
            "date_required": True,
            "datasets": [
                {
                    "name": DATASET_NAME_DEFAULT,
                    "name_original": DATASET_NAME_DEFAULT,
                    "grouped": True,
                    "parameters": [
                        {
                            "name": "temperature_air_max_2m_mean",
                            "name_original": "mean max temp (°c)",
                            "unit_type": "temperature",
                            "unit": "degree_celsius",
                        },
                        {
                            "name": "quality_temperature_air_max_2m_mean",
                            "name_original": "mean max temp flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "temperature_air_min_2m_mean",
                            "name_original": "mean min temp (°c)",
                            "unit_type": "temperature",
                            "unit": "degree_celsius",
                        },
                        {
                            "name": "quality_temperature_air_min_2m_mean",
                            "name_original": "mean min temp flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "temperature_air_mean_2m",
                            "name_original": "mean temp (°c)",
                            "unit_type": "temperature",
                            "unit": "degree_celsius",
                        },
                        {
                            "name": "quality_temperature_air_mean_2m",
                            "name_original": "mean temp flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "temperature_air_max_2m",
                            "name_original": "extr max temp (°c)",
                            "unit_type": "temperature",
                            "unit": "degree_celsius",
                        },
                        {
                            "name": "quality_temperature_air_max_2m",
                            "name_original": "extr max temp flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "temperature_air_min_2m",
                            "name_original": "extr min temp (°c)",
                            "unit_type": "temperature",
                            "unit": "degree_celsius",
                        },
                        {
                            "name": "quality_temperature_air_min_2m",
                            "name_original": "extr min temp flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "precipitation_height_liquid",
                            "name_original": "total rain (mm)",
                            "unit_type": "precipitation",
                            "unit": "millimeter",
                        },
                        {
                            "name": "quality_precipitation_height_liquid",
                            "name_original": "total rain flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "snow_depth_new",
                            "name_original": "total snow (cm)",
                            "unit_type": "length_short",
                            "unit": "centimeter",
                        },
                        {
                            "name": "quality_snow_depth_new",
                            "name_original": "total snow flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "precipitation_height",
                            "name_original": "total precip (mm)",
                            "unit_type": "precipitation",
                            "unit": "millimeter",
                        },
                        {
                            "name": "quality_precipitation_height",
                            "name_original": "total precip flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "snow_depth",
                            "name_original": "snow grnd last day (cm)",
                            "unit_type": "length_short",
                            "unit": "centimeter",
                        },
                        {
                            "name": "quality_snow_depth",
                            "name_original": "snow grnd last day flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "wind_direction_gust_max",
                            "name_original": "dir of max gust (10s deg)",
                            "unit_type": "angle",
                            "unit": "degree",
                        },
                        {
                            "name": "quality_wind_direction_gust_max",
                            "name_original": "dir of max gust flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                        {
                            "name": "wind_gust_max",
                            "name_original": "spd of max gust(km/h)",
                            "unit_type": "speed",
                            "unit": "kilometer_per_hour",
                        },
                        {
                            "name": "quality_wind_gust_max",
                            "name_original": "spd of max gust flag",
                            "unit_type": "dimensionless",
                            "unit": "dimensionless",
                        },
                    ],
                }
            ],
        },
        {
            "name": "annual",
            "name_original": "annual",
            "periods": ["historical"],
            "date_required": True,
            "datasets": [
                {
                    "name": DATASET_NAME_DEFAULT,
                    "name_original": DATASET_NAME_DEFAULT,
                    "grouped": True,
                    "parameters": [
                        {
                            "name": "temperature_air_max_2m_mean",
                            "name_original": "average max. temp. (°c)",
                            "unit_type": "temperature",
                            "unit": "degree_celsius",
                        },
                        {
                            "name": "temperature_air_min_2m_mean",
                            "name_original": "average min. temp. (°c)",
                            "unit_type": "temperature",
                            "unit": "degree_celsius",
                        },
                        {
                            "name": "precipitation_frequency",
                            "name_original": "frequency of precip. (%)",
                            "unit_type": "fraction",
                            "unit": "percent",
                        },
                        {
                            "name": "temperature_air_max_2m",
                            "name_original": "highest temp. (°c)",
                            "unit_type": "temperature",
                            "unit": "degree_celsius",
                        },
                        {
                            "name": "temperature_air_min_2m",
                            "name_original": "lowest temp. (°c)",
                            "unit_type": "temperature",
                            "unit": "degree_celsius",
                        },
                        {
                            "name": "precipitation_height_max",
                            "name_original": "greatest precip. (mm)",
                            "unit_type": "precipitation",
                            "unit": "millimeter",
                        },
                        {
                            "name": "precipitation_height_liquid_max",
                            "name_original": "greatest rainfall (mm)",
                            "unit_type": "precipitation",
                            "unit": "millimeter",
                        },
                        {
                            "name": "snow_depth_new_max",
                            "name_original": "greatest snowfall (cm)",
                            "unit_type": "length_short",
                            "unit": "centimeter",
                        },
                        {
                            "name": "snow_depth_max",
                            "name_original": "most snow on the ground (cm)",
                            "unit_type": "length_short",
                            "unit": "centimeter",
                        },
                    ],
                }
            ],
        },
    ]
}
EcccObservationMetadata = build_metadata_model(EcccObservationMetadata, "EcccObservationMetadata")
