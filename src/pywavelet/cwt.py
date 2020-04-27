import math
import numpy as np
import scipy.fftpack as fft

def compute_scale_range(s0, dj, j1):
    return np.array([s0 * 2 ** (j * dj) for j in range(j1)])

def wavelet(data, dt, scales, wavelet, file=open('/dev/stdout','w')):
    
    N = data.size
    # Pad data with zeros on two sides
    data_padded = np.concatenate([np.zeros(int(data.size/2)), data, np.zeros(int(data.size/2))])
    x_k = fft.fft(data_padded) / data_padded.size
    w_k = np.arange(0, data_padded.size) * 2 * np.pi / (data_padded.size) / dt
    w_k[N:] = w_k[N:]*(-1)
    # construct Wn matrix 
    Psi_hat =  np.concatenate([wavelet.psi_hat(w_k, s, dt, normalized=True)[np.newaxis, :] \
                              for s in scales], axis=0)
    A = x_k[np.newaxis,:] * Psi_hat
    del Psi_hat
    W_n = data_padded.size * np.fft.ifft(A)[:,data_padded.astype(bool)]
    return W_n

def reconstruct_signal(W_n, wavelet, scales, dj, dt):
    scaling_factor = dj * dt**0.5 / (wavelet.C_delta * wavelet.psi_0_0)
    return scaling_factor * (np.real(W_n) / scales[:,np.newaxis]**0.5).sum(axis=0)

def compute_energy_density(W_n, scales):
    return np.abs(W_n * W_n.conjugate()) / scales[:,np.newaxis]**0.5

