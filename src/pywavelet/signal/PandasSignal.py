from pandas import Series
from .base import BaseSignal

class PandasSignal(BaseSignal):

    # Implementations of abstract method
    @property
    def index(self):
        return self._data.index

    @index.setter
    def index(self, index):
        self._data.index = index

    @property
    def values(self):
        return self._data.values

    @values.setter
    def values(self, values):
        self._data.values = values

    def test_index_equal_spaced(self):
        index_diff = self.index[1:] - self.index[:-1]
        return not any(index_diff / index_diff[0] - 1)

    def test_no_missing_value(self):
        return not self._data.isna().sum()
