'''
Base class for all wavelets.
'''
from __future__ import annotations
from abc import ABC, abstractmethod
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

    @staticmethod
    @abstractmethod
    def scale_to_period(scale):
        pass

    @staticmethod
    @abstractmethod
    def period_to_scale(period):
        pass


