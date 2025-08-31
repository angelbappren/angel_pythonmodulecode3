from load import load_for_csv
import pandas as pd


def test_load_for_csv_successful(tmp_path):
    df = pd.DataFrame({"RequestID": [1, 2], "AllocatedUser": ["Amy", "John"]})
    output_file = tmp_path / "outputs" / "result.csv"
    result = load_for_csv(df, output_file)

    #return path and file exists
    assert result == str(output_file)
    assert output_file.exists()

    #file content correct/matches
    saved = pd.read_csv(output_file)

    assert list(saved.columns) == ["RequestID", "AllocatedUser"]
    assert len(saved) == 2
    assert saved.iloc[0]["AllocatedUser"] == "Amy"


    def test_load_for_csv_empty_df(tmp_path):
        df = pd.DataFrame(columns=["A", "B"])
        output_file = tmp_path / "empty" "empty.csv"
        result = load_for_csv(df, output_file)

        assert result == str(output_file)
        assert output_file.exists()

        saved = pd.read_csv(output_file)
        assert list(saved.columns) == ["A", "B"]
        assert len(saved) == 0


