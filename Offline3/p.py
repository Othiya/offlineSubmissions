import numpy as np
import matplotlib.pyplot as plt

# Define the functions as before
def parabolic(x):
    return np.where((x >= -2) & (x <= 2), x**2, 0)

def rectangle(x):
    return np.where((x >= -2) & (x <= 2), 1, 0)

def triangle(x):
    return np.where((-2 <= x) & (x <= 2), 1 - np.abs(x) / 2, 0)

def sawtooth(x):
    return np.where((-2 <= x) & (x <= 2), x, 0)

# Define the interval and function to sample
x_values = np.linspace(-10, 10, 1000)
y_values = parabolic(x_values)  # Choose the sawtooth function for this example

# Plot the original function
plt.figure(figsize=(12, 4))
plt.plot(x_values, y_values, label="Sawtooth Function")
plt.title("Original Function (Sawtooth)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

# Define the sampled times and frequencies
sampled_times = x_values
frequencies = np.linspace(-5, 5, 1000)  # Frequency domain for Fourier transform

# Fourier Transform using numerical integration (trapezoidal rule)
def fourier_transform(signal, frequencies, sampled_times):
    dt = sampled_times[1] - sampled_times[0]  # Assuming uniform sampling
    num_freqs = len(frequencies)
    ft_result_real = np.zeros(num_freqs)
    ft_result_imag = np.zeros(num_freqs)
    
    # Numerical integration using the trapezoidal rule
    for i, f in enumerate(frequencies):
        real_part = np.trapz(signal * np.cos(2 * np.pi * f * sampled_times), sampled_times)
        imag_part = np.trapz(signal * (-np.sin(2 * np.pi * f * sampled_times)), sampled_times)
        
        ft_result_real[i] = real_part
        ft_result_imag[i] = imag_part
    
    return ft_result_real, ft_result_imag

# Apply Fourier Transform
ft_real, ft_imag = fourier_transform(y_values, frequencies, sampled_times)

# Plot the magnitude of the Fourier Transform
plt.figure(figsize=(12, 6))
plt.plot(frequencies, np.sqrt(ft_real**2 + ft_imag**2))
plt.title("Magnitude of Fourier Transform (Sawtooth Function)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()

# Inverse Fourier Transform
def inverse_fourier_transform(ft_real, ft_imag, frequencies, sampled_times):
    dt = sampled_times[1] - sampled_times[0]  # Sampling interval
    n = len(sampled_times)
    reconstructed_signal = np.zeros(n)
    
    # Numerical inverse Fourier transform using the trapezoidal rule
    for i, t in enumerate(sampled_times):
        real_part = np.trapz(ft_real * np.cos(2 * np.pi * frequencies * t), frequencies)
        imag_part = np.trapz(ft_imag * np.sin(2 * np.pi * frequencies * t), frequencies)
        
        reconstructed_signal[i] = real_part + imag_part
    
    return reconstructed_signal

# Reconstruct the signal from the FT data
reconstructed_y_values = inverse_fourier_transform(ft_real, ft_imag, frequencies, sampled_times)

# Plot the original and reconstructed functions for comparison
plt.figure(figsize=(12, 4))
plt.plot(x_values, y_values, label="Original Sawtooth Function", color="blue")
plt.plot(sampled_times, reconstructed_y_values, label="Reconstructed Sawtooth Function", color="red", linestyle="--")
plt.title("Original vs Reconstructed Sawtooth Function")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
