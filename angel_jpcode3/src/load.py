import pandas as pd
import logging
import logging.config
from pathlib import Path
import sys

config_path = Path(__file__).resolve().parent.parent / "logging.ini"
logging.config.fileConfig(config_path, defaults={"logfilename": "app.log"})


def load_for_csv(df: pd.DataFrame, output_path) -> str:
    try:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False)

        logging.info(f"DataFrame with new {len(df)} rows written to '{output_path}'.")
        return str(output_path)

    except Exception as save_summary_error:
        logging.error(f"Failed to save DataFrame to the identified '{output_path}': {str(save_summary_error)}")
        return ""