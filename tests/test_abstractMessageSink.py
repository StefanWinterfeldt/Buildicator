import pytest
from messageSinks.abstractMessageSink import AbstractMessageSink


def test_notOverwritingShowStatusCausesNotImplementedError():
    class TestMessageSink(AbstractMessageSink):
        def __init__(self):
            pass

    testMessageSink = TestMessageSink()
    with pytest.raises(NotImplementedError):
        testMessageSink.showStatus(0)
