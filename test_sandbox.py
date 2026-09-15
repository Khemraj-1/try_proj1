import time

def test_this_will_hang():
    time.sleep(120)
    assert True
