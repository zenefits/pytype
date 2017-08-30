"""Python code corresponding to PYTHONCODE entries in __builtin__.pytd.

Each PYTHONCODE item in __builtin__.pytd will have a single python `def` here.
"""


# pylint: disable=redefined-builtin
# pylint: disable=invalid-name
# pylint: disable=unused-argument
# pylint: disable=undefined-variable


class classmethod(object):
  """Classmethod method decorator."""

  def __init__(self, func):
    # Name the inner method __func__, like in Python/Objects/funcobject.c
    self.__func__ = func

  def __get__(self, obj, objtype):
    func = self.__func__
    def method(*args, **kwargs):
      return func(objtype, *args, **kwargs)
    return method
