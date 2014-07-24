import random
from connectors.dummyConnector import DummyConnector


def test_getStatus():
    random.choice = lambda x: 0
    connector = DummyConnector(None)
    assert 0 == connector.getStatus()
