'''
Base class for all wavelets.
'''
from __future__ import annotations
from abs import ABC, abstractmethod
import numpy as np
import scipy.special

class BaseWavelet(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def psi(self):
        pass

    @abstractmethod
    def psi_hat(self):
        pass

    @abstractmethod
    @staticmethod
    def scale_to_period(scale):
        pass

    @abstractmethod
    @staticmethod
    def period_to_scale(period):
        pass


