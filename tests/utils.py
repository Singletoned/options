import sys
import contextlib

import mock


@contextlib.contextmanager
def raises(error):
    try:
        yield
    except error:
        pass

class MockError(Exception):
    pass

def mock_onabort(msg):
    raise MockError(msg)

class MockStdErr(object):
    _data = []

    def write(self, text):
        self._data.append(text)

stderr_patcher = mock.patch.object(
    sys, 'stderr', MockStdErr())
