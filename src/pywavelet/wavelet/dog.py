import numpy as np
import scipy.special
from .base import BaseWavelet

class WaveletDOG(BaseWavelet):

    def __init__(self, m=2):
        self.m = m
        self.name = 'DOG'

    def psi_hat(self, omega, scale, delta_t, normalized=True):
        """
        Input:
            To be completed...
        """
        m = self.m
        m_hat0 = -1j ** m / np.sqrt(scipy.special.gamma(m + 0.5)) * (scale * omega) ** m \
                * np.exp(-(scale * omega)**2 /2)

        if normalized == True:
            m_hat0 *= (2 * np.pi * scale / delta_t) ** 0.5
        return m_hat0

    def scale_to_period(self, scale):
        return 2 * np.pi * scale / np.sqrt(self.m + 0.5)

    @staticmethod
    def scale_to_coi(scale):
        return np.sqrt(2) * scale
