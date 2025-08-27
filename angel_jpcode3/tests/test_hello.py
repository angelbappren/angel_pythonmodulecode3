from fun.hello import say_hello

def test_say_hello(caplog):
    with caplog.at_level("INFO"):
        result = say_hello("Angel")

    assert result == "Hello, Angel!"

    assert any("Generated greeting" in rec.getMessage() for rec in caplog.records)