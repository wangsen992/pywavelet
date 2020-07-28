'''Base class for holding and (pre)processing the input (1D) signal

This signal class should be able to handle index both in distance and/or time,
therefore index should be consturcted out of a different object. A structural
pattern should probably be used to handle the different implementation.
'''
from __future__ import annotations
from abc import ABC, abstractmethod

class BaseSignal(ABC):

    # Private methods
    def _validate(self):
        '''Make sure data are equal-spaced (index) and there is no missing
        value'''
        
        assert self.test_index_equal_spaced(), "Index must be equally spaced"
        assert self.test_no_missing_value(), "There should be no missing value"

        return True

    # Public methods (to be inherited for general use)
    def __init__(self, data):
        self._data = data
        self._validate()

    def plot(self, *args, **kwargs):
        '''Invoke plot method of internals, overwrite if needed'''
        return self._data.plot(*args, **kwargs)

    def __repr__(self):
        return f"Internal: {type(self._data)}\n" + self._data.__repr__()

    # Public method interfaces (need to implement)
    @property
    @abstractmethod
    def index(self):
        '''Get index object of the internal data structure'''
        pass

    @index.setter
    @abstractmethod
    def index(self, index):
        pass

    @property
    @abstractmethod
    def values(self):
        '''Get value object of the internal data structure'''
        pass

    @values.setter
    @abstractmethod
    def values(self):
        pass


    @abstractmethod
    def test_index_equal_spaced(self):
        pass

    @abstractmethod
    def test_no_missing_value(self):
        pass

