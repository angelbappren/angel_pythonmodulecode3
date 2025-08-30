import pandas as pd
import logging

def extract_source(filepath, file_type='csv', sheet_name=0):
    
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
        return pd.DataFrame()  