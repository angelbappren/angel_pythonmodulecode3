from transform import stitch_year_files
import pandas as pd

def test_stitch_year_files(tmp_path):
    y1 = tmp_path / "2023.csv"
    y2 = tmp_path / "2024.csv"
    y1.write_text("RequestID,AllocatedUser\n1,Amy\n2,Bob\n")
    y2.write_text("RequestID,AllocatedUser\n3,Tom\n4,Anne\n")

    df = stitch_year_files([str(y1), str(y2)], batch_load="30-08-2025")

    assert not df.empty
    assert list(df.columns) == ["RequestID", "AllocatedUser", "BatchLoad"]
    assert len(df) == 4
    assert set(df["BatchLoad"].unique()) == {"30-08-2025"}


def test_stitch_year_files_mismatch_cols(tmp_path):
    y1 = tmp_path / "a.csv"
    y2 = tmp_path / "b.csv"
    y1.write_text("RequestID,AllocatedUser\n1,Amy\n")
    y2.write_text("ID,Item\n2,Laptop\n")

    df = stitch_year_files([str(y1), str(y2)], batch_load="30-08-2025")

    assert set(df.columns) == {"RequestID", "AllocatedUser", "ID", "Item", "BatchLoad"}
    assert len(df) == 2
    assert df["BatchLoad"].iloc[0] == "30-08-2025"


def test_stitch_year_files_skip_invalid_file(tmp_path):
    ok = tmp_path / "good.csv"
    not_ok = tmp_path / "bad.csv" # missing file removed
    ok.write_text("RequestID,AllocatedUser\n1,Amy\n")

    df = stitch_year_files([str(ok), str(not_ok)], batch_load="30-08-2025")

    assert len(df) == 1
    assert "BatchLoad" in df.columns


def test_stitch_year_files_all_error(tmp_path):
    df = stitch_year_files([str(tmp_path / "all_error.csv")], batch_load="30-08-2025")
    assert df.empty


