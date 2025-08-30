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



        logging.info(f"{file_type.upper()} file '{filepath}' extracted successfully with {len(df)} rows.")


        #logging.info("✅✅✅ Test log line triggered ✅✅✅")



        return df
    

    except Exception as error:
        logging.error(f"Failed to load {file_type.upper()} file '{filepath}': {str(error)}")
        return pd.DataFrame()  