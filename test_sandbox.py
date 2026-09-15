import urllib.request

def test_network_should_be_blocked():
    urllib.request.urlopen("http://example.com", timeout=5)
