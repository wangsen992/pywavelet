'''
Base class for Fourier transforms.

Idea is that Fourier transform is the major performance hurdle, therefore for
performance reasons it needs to have a plug-and-perform flexibility.

Strategy pattern is used here to isolate the FFT implementations (as FFTSolver
object) and the client-facing interface (FFT). 
'''
from __future__ import annotations
from abc import ABC, abstractmethod

class FFT:
    def __init__(self, fft_solver : FFTSolver):
        self._fft_solver = FFTSolver

    @property
    def fft_solver(self):
        return self._fft_solver

    @fft_solver.setter
    def fft_solver(self, fft_solver : FFTSolver):
        self._fft_solver = fft_solver

    def pad_data(self, data):
        '''Padding data with zeros on both sides'''
        raise NotImplementedError
    

class FFTSolver(ABC):

    @staticmethod
    @abstractmethod
    def fft(x):
        pass

    @staticmethod
    @abstractmethod
    def ifft(x):
        pass

