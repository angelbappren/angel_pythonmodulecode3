import pandas as pd
import logging
from pathlib import Path


def load_for_csv(df: pd.DataFrame, output_path) -> str:
    try:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False)

        logging.info(f"DataFrame with {len(df)} rows written to '{output_path}'.")
        return str(output_path)

    except Exception as save_summary_error:
        logging.error(f"Failed to save DataFrame to '{output_path}': {str(save_summary_error)}")
        return ""