import numpy as np
import scipy.special 

class WaveletMorlet(object):

    
    def __init__(self, omega_0=6):
        self.omega_0 = omega_0
        self.name = 'Morlet'
        self.psi_0_0 = np.pi ** (-0.25)
        self.C_delta = 0.776
        self.gamma = 2.32
        self.dj_0 = 0.60
    
    def psi(self, del_t, scale, delta_t, normalized=True):
        """
        Input:
            del_t:      1d-array, time/position offset
            scale:      float,
            delta_t:    float, resolution
            omega_0:    parameter for morlet wavelet
            normalized: bool. 
        """
        eta = del_t / scale
        m0 = np.pi ** (-0.25) * np.exp(1j * self.omega_0 * eta - eta**2 / 2)
        if normalized == True:
            m0 *= (delta_t / scale) ** 0.5
        return m0

    def psi_hat(self, omega, scale, delta_t, normalized=True):
        m_hat0 = np.pi**(-0.25) * np.heaviside(omega,0) * \
                np.exp(-(scale * omega - self.omega_0)**2/2)
        if normalized == True:
            m_hat0 *= (2 * np.pi * scale / delta_t) ** 0.5
        return m_hat0

    @staticmethod
    def scale_to_period(scale):
        return 4 * np.pi * scale / (6 + np.sqrt(2 + 6**2))

    @staticmethod
    def scale_to_coi(scale):
        return np.sqrt(2) *scale

class WaveletDOG(object):

    def __init__(self, m=2):
        self.m = m
        self.name = 'DOG'

    def psi_hat(self, omega, scale, delta_t, normalized=True):
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
