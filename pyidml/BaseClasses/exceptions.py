class pyidmlException(Exception):
    """Base-class for all exceptions raised by this module"""


class NotParaException(pyidmlException):
    """Expected a paragraph tag, received something else"""
