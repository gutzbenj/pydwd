""" function to read data from dwd server """
from datetime import datetime as dt
from pathlib import Path
from typing import List
from zipfile import ZipFile
from io import BytesIO

import pandas as pd

from python_dwd.additionals.functions import check_parameters
from python_dwd.additionals.functions import determine_parameters
from python_dwd.constants.column_name_mapping import DATE_NAME, \
    GERMAN_TO_ENGLISH_COLUMNS_MAPPING
from python_dwd.constants.metadata import STATIONDATA_MATCHSTRINGS


def parse_dwd_data(files_in_bytes: List[BytesIO],
                   write_file: bool = False) -> pd.DataFrame:
    """
    This function is used to read the stationdata for which the local zip link is
    provided by the 'download_dwd' function. It checks the zipfile from the link
    for its parameters, opens every zipfile in the list of files and reads in the
    containing product file, and if there's an error or it's wanted the zipfile is
    removed afterwards.

    Args:
        local_files: list of local stored files that should be read
        keep_zip: If true: The raw zip file will not be deleted, Default is: False.

    Returns:
        DataFrame with requested data

    """
    # Test for types of input parameters
    assert isinstance(files_in_bytes, list)
    assert isinstance(write_file, bool)

    # Check for files and if empty return empty DataFrame
    if not files_in_bytes:
        return pd.DataFrame()

    # first_filename = str(local_files[0]).split("/")[-1]
    #
    # parameter, time_resolution, period_type = determine_parameters(first_filename)
    # check_parameters(parameter, time_resolution, period_type)

    data = []

    for file in files_in_bytes:
        try:
            data_file = pd.read_csv(filepath_or_buffer=file,
                                    sep=";",
                                    na_values="-999")

            data.append(data_file)

        except pd.errors.ParserError as e:
            print(f"The file could be parsed to a dataframe."
                  f"Error: {str(e)}")

    # Put together list of files to a DataFrame
    data = pd.concat(data)

    # Extract column names
    column_names = data.columns

    # Strip empty chars from before and after column names
    column_names = [column_name.upper().strip()
                    for column_name in column_names]

    # Replace certain names by conform names
    column_names = [GERMAN_TO_ENGLISH_COLUMNS_MAPPING.get(column_name, column_name)
                    for column_name in column_names]

    # Reassign column names to DataFrame
    data.columns = column_names

    # String to date
    data[DATE_NAME] = data[DATE_NAME].apply(
        lambda date: dt.strptime(str(date), "%Y%m%d"))

    if write_file:
        pass

    return data
