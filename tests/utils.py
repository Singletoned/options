import sys
import contextlib


@contextlib.contextmanager
def raises(error):
    try:
        yield
    except error:
        pass
