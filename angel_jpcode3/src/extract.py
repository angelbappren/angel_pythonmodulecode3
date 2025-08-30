import pandas as pd
import logging

def extract_source(filepath, file_type='csv', sheet_name=0):
    """
    Extracts data from a CSV or Excel file.

    Args:
        filepath (str): File path to load.
        file_type (str): 'csv' or 'excel'
        sheet_name (int or str): Sheet name or index (only used for Excel)

    Returns:
        pd.DataFrame: Loaded DataFrame, or empty if failed.
    """
    try:
        if file_type == "csv":
            df = pd.read_csv(filepath)
        elif file_type == "excel":
            df = pd.read_excel(filepath, sheet_name=sheet_name)
        else:
            raise ValueError("Unsupported file type: must be 'csv' or 'excel'.")

        logging.info(f"Loaded {file_type.upper()} file: '{filepath}' with {len(df)} rows.")
        return df

    except Exception as error:
        logging.error(f"Failed to load {file_type.upper()} file '{filepath}': {str(error)}")
        return pd.DataFrame()  # <- Note the capital 'F'