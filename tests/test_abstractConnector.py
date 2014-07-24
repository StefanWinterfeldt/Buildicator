import pytest
from connectors.abstractConnector import AbstractConnector


def test_notOverwritingGetStatusCausesNotImplementedError():
    class TestConnector(AbstractConnector):
        def __init__(self):
            pass

    testConnector = TestConnector()
    with pytest.raises(NotImplementedError):
        testConnector.getStatus()