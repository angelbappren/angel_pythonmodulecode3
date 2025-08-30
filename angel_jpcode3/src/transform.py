import pandas as pd
import logging

def stitch_year_files(file_list, load_date):

    year_files = []

    for path in file_list:
        try:
            df = pd.read_csv(path)
            logging.info(f"Loaded CSV '{path}' with {len(df)} rows.")
            year_files.append(df)
        except Exception as fail_error:
            logging.error(f"Failed to load CSV '{path}': {str(fail_error)}")

    if not year_files:
        logging.warning("No CSV files successfully loaded; returning empty df.")
        return pd.DataFrame()
    
stitched = pd.concat(year_files, ignore_index=True, sort=False)
stitched["BatchLoad"] = batch_load
logging.info(f"Stitched {len(year_files)} files/s") → {len(stitched) total rows. BatchLoad='{batch_load}'}
return stitched

