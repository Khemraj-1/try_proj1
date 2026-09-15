def test_basic_math():
    assert 2 + 2 == 4

def test_this_should_fail():
    result = 10 / 2
    assert result == 4, f"Expected 4, got {result}"
