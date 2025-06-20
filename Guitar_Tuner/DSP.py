import numpy as np
import matplotlib.pyplot as plt


sampling_rate = 440
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
    fft = np.fft.rfft(hamming_signal)
    # Calculate the magnitude spectrum
    magnitude = np.abs(fft)
    # Get the index of the maximum magnitude 
    max_index = np.argmax(magnitude)
    # Determine the frequency bins
    freqeuencies = np.fft.rfftfreq(len(signal), 1 / fs)
    max_freq = freqeuencies[max_index]
    return max_freq 

    
def detect_pitch_autocorr(signal, fs):
    # Estimate the pitch using autocorrelation
    hamming = apply_hamming(signal)    
    mean = np.mean(hamming)
    hamming = hamming - mean

    # Do the auto correlation
    correlation = np.correlate(hamming, hamming, mode = "full")
    correlation = correlation[len(signal):]
    start_index = np.where(np.diff(correlation) > 0)[0][0]
    peak_index = np.argmax(correlation[start_index:]) + start_index
    

    
   # Find the first real peak after lag 0
    return fs / peak_index