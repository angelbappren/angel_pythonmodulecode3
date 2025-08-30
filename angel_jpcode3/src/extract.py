import pandas as pd
import logging

def extract_source():

    try:
        if file_type == "csv"

        elif file_type == "excel"

        else:
            raise ValueError(f"Unsupported file type: must be csv or excel.")
        

        logging.info(f"Loaded {file_type.upper()} file: "{filepath}" with {len(df)} rows.") return df 

    except Exception as error:
        logging.error(f"Failed to load {file_type.upper()} file: "{filepath}": {(str(error)}") return pd.Dataframe()

