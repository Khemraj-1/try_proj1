import requests

def test_basic_math():
    assert 2 + 2 == 4

def test_dependency_installed():
    assert requests.__version__
