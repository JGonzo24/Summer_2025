import matplotlib.pyplot as plt
import numpy as np

from DSP import detect_pitch_autocorr, detect_pitch_fft

fs = 44100
f = 440
duration = 1.0

t = np.linspace(0,duration, int(fs * duration), endpoint = False)

# Generate signal
signal = np.sin(2 * np.pi * f * t)

# Run pitch detection
pitch_fft = detect_pitch_fft(signal, fs)
pitch_autocorr = detect_pitch_autocorr(signal, fs)

print(f"True Frequency {f} Hz")
print(f"FFT Estimate {pitch_fft:.2f} Hz")
print(f"Autocorr estimate: {pitch_autocorr:.2f} Hz")
