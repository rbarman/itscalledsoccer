from  client import AmericanSoccerAnalysis

def test_get_stadia():
    client = AmericanSoccerAnalysis()
    assert client.lazy_load == True
    assert client.stadia is None
    stadia = client.get_stadia(leagues=['mls'])
    assert stadia is not None

def test_get_referees():
    client = AmericanSoccerAnalysis()
    assert client.lazy_load == True
    assert client.referees is None
    referees = client.get_referees(leagues=['mls'])
    assert referees is not None

def test_get_managers():
    client = AmericanSoccerAnalysis()
    assert client.lazy_load == True
    assert client.managers is None
    managers = client.get_managers(leagues=['mls'])
    assert managers is not None

def test_get_teams():
    client = AmericanSoccerAnalysis()
    assert client.lazy_load == True
    assert client.teams is None
    teams = client.get_teams(leagues=['mls'])
    assert teams is not None

def test_get_players():
    client = AmericanSoccerAnalysis()
    assert client.lazy_load == True
    assert client.players is None
    players = client.get_players(leagues=['mls'])
    assert players is not None


if __name__ == '__main__':
    # TODO: migrate to actual test setup in tests/ ?
    test_get_stadia()
    test_get_referees()
    test_get_managers()
    test_get_teams()
    test_get_players()

