from extract import extract_source
import pandas as pd

def test_extract_source_csv_working(tmp_path):
    
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text("RequestID,AllocatedUser\n1234,Amy\n5678,John\n")

    df = extract_source(str(csv_file), file_type="csv")

    assert not df.empty
    assert list(df.columns) == ["RequestID", "AllocatedUser"]
    assert len(df) == 2

def test_extract_source_excel_working(tmp_path):
    
    excel_path = tmp_path / "trial.xlsx"
    pd.DataFrame({
        "RequestID": [1234, 5678],
        "AllocatedUser": ["Amy", "John"]
    }).to_excel(excel_path, index=False)

    df = extract_source(str(excel_path), file_type="excel")

    assert not df.empty
    assert list(df.columns) == ["RequestID", "AllocatedUser"]
    assert len(df) == 2

def test_extract_source_unsupported_file_type():
    
    df = extract_source("fake_path.json", file_type="json")
    assert df.empty
