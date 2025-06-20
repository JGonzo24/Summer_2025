import numpy as np
import matplotlib.pyplot as plt

def apply_hamming(signal):
    # apply a hamming window function to reduce the spectral leakage here
    if (len(signal) == 0):
        raise ValueError("The signal is zero!")
    hamming = np.hamming(len(signal)) * signal
    return hamming

def detect_pitch_fft(signal, fs):
    # Estimate the pitch using FFT analysis
    hamming_signal = apply_hamming(signal)

    # Compute the FFT to turn from time domain signal into frequency domain
    fft = np.fft.fft(hamming_signal)
    # Calculate the magnitude spectrum
    magnitude = np.abs(fft)
    # Determine the frequency bins
    
    pass

def detect_pitch_autocorr(signal, fs):
    # Estimate the pitch using autocorrelation

    pass


