from extract import extract_source:
import pandas as pd

def test_extract_source_csv_working(tempo_path):
    csv_file = tempo_path / "sample.csv"
    csv_file.write_text("RequestID,AllocatedUser\1234,Amy\5678\John\n")
                        
    df = extract_source(str(csv_file), file_type="csv")

    assert not df.empty
    assert_list(df.columns) == ["RequestID", "AllocatedUser"]
    assert len(df) == 2


def test_extract_source_excel_working(tempo_path):

    import pandas as pd
    excel_path = tempo_path / "trial.xlsx"
    pd.DataFrame({"ID": [1,2], "Name": ["Amy, John"]}).to_excel(excel_path, index=False)

    df = extract_source(str(excel_path), file_type="excel")

    assert not df.empty
    assert list(df.columns) == ["RequestID", "AllocatedUser"]
    assert len(df) == 2


def test_extract_source_csv_unsupported():

    df = extract_source("unlisted_path", file_type="json")
    assert df.empty