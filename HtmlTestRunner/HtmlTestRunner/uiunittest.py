import unittest

__unittest = True

_MAX_LENGTH = 80
def safe_repr(obj, short=False):
    try:
        result = repr(obj)
    except Exception:
        result = object.__repr__(obj)
    if not short or len(result) < _MAX_LENGTH:
        return result
    return result[:_MAX_LENGTH] + ' [truncated]...'

class UITestCase(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super(UITestCase, self).__init__(methodName)
        pass

    def fail(self, msg=None, expectedImageFile="", actualImageFile=""):
        """Fail immediately, with the GIVEN message."""
        msg = self._failformatMessage(msg, expectedImageFile, actualImageFile)
        raise self.failureException(msg)

    def _failformatMessage(self, msg, expectedImageFile, actualImageFile):
        """Honour the longMessage attribute when generating failure messages.
        If longMessage is False this means:
        * Use only an explicit message if it is provided
        * Otherwise use the standard message for the assert

        If longMessage is True:
        * Use the standard message
        * If an explicit message is provided, plus ' : ' and the explicit message
        """

        # if not self.longMessage:
        #     return msg or standardMsg
        if expectedImageFile is None:
            return msg
        elif actualImageFile is None:
            return msg

        try:
            # don't switch to '{}' formatting in Python 2.X
            # it changes the way unicode input is handled
            return '%s sep:sep %s sep:sep %s' % (msg, expectedImageFile, actualImageFile)
        except UnicodeDecodeError:
            return '%s sep:sep %s sep:sep %s' % (safe_repr(msg), safe_repr(expectedImageFile), safe_repr(actualImageFile))