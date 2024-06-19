from  client import AmericanSoccerAnalysis

def test_get_stadia():
    client = AmericanSoccerAnalysis(lazy_load=True)
    print(f"lazy load: {client.lazy_load}")
    print(f"stadia: {client.stadia}")
    
    assert client.lazy_load == True
    assert client.stadia is None

    stadia = client.get_stadia(leagues=['mls'])
    assert stadia is not None

if __name__ == '__main__':
    test_get_stadia()

