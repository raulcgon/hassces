#
# (C) Copyright 2015 Enthought, Inc., Austin, TX
# All right reserved.
#
# This file is open source software distributed according to the terms in
# LICENSE.txt
#

""" Utility functions to help with cffi wrapping.
"""


from cffi import FFI

ffi = FFI()
ffi.set_unicode(True)


def HMODULE(cdata):
    return int(ffi.cast("intptr_t", cdata))


def PVOID(x):
    return ffi.cast("void *", x)


def IS_INTRESOURCE(x):
    """ Check if x is an index into the id list.

    """
    return int(ffi.cast("uintptr_t", x)) >> 16 == 0


def RESOURCE(resource):
    """ Convert a resource into a compatible input for cffi.

    """
    if isinstance(resource, int):
        resource = ffi.cast('wchar_t *', resource)
    elif isinstance(resource, str):
        resource = str(resource)
    return resource


def resource(lpRESOURCEID):
    """ Convert the windows RESOURCE into a python friendly object.
    """
    if IS_INTRESOURCE(lpRESOURCEID):
        resource = int(ffi.cast("uintptr_t", lpRESOURCEID))
    else:
        resource = ffi.string(lpRESOURCEID)
    return resource


class ErrorWhen(object):
    """ Callable factory for raising errors when calling cffi functions.

    """

    def __init__(self, check, raise_on_zero=True):
        """ Constructor

        Parameters
        ----------
        check :
            The return value that designates that an error has taken place.

        raise_on_zero : bool
            When set any error will be raised. When false the winerror
            is checked and only non-zero win errors are raised. Currently
            this parameters is used to workaround issues with the win32
            implementation in ``wine``.

        """
        self._check = check
        self._raise_on_zero = raise_on_zero

    def __call__(self, value, function_name=''):
        if value == self._check:
            self._raise_error(function_name)
        else:
            return value

    def _raise_error(self, function_name=''):
        code, message = ffi.getwinerror()
        exception = WindowsError()
        exception.errno = ffi.errno
        exception.winerror = code
        exception.strerror = message
        exception.function = function_name
        raise exception


check_null = ErrorWhen(ffi.NULL)
check_zero = ErrorWhen(0)
check_false = ErrorWhen(False)
