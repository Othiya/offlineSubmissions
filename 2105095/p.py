import numpy as np
import matplotlib.pyplot as plt

# Define the interval and function and generate appropriate x values and y values
x_values = np.linspace(-10, 10, 1000)  # Define x over the range [-10, 10]
y_values = x_values**2  # Define the function y = x^2

# Plot the original function
plt.figure(figsize=(12, 4))
plt.plot(x_values, y_values, label="Original y = x^2", color='blue')
plt.title("Original Function (y = x^2)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# Define the sampled times and frequencies
sampled_times = x_values
frequencies = np.linspace(-5, 5, 1000)  # Frequencies range [-5 Hz, 5 Hz]

# Fourier Transform
def fourier_transform(signal, frequencies, sampled_times):
    num_freqs = len(frequencies)
    ft_result_real = np.zeros(num_freqs)
    ft_result_imag = np.zeros(num_freqs)
    dt = sampled_times[1] - sampled_times[0]  # Time step size
    
    for i, freq in enumerate(frequencies):
        # Calculate the real and imaginary parts using trapezoidal integration
        cosine_term = np.cos(2 * np.pi * freq * sampled_times)
        sine_term = np.sin(2 * np.pi * freq * sampled_times)
        ft_result_real[i] = np.trapz(signal * cosine_term, sampled_times)
        ft_result_imag[i] = np.trapz(signal * sine_term, sampled_times)
    
    return ft_result_real, ft_result_imag

# Apply FT to the sampled data
ft_data = fourier_transform(y_values, frequencies, sampled_times)

# Plot the FT data
plt.figure(figsize=(12, 6))
plt.plot(frequencies, np.sqrt(ft_data[0]**2 + ft_data[1]**2), label="Magnitude Spectrum", color='red')
plt.title("Frequency Spectrum of y = x^2")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# Inverse Fourier Transform
def inverse_fourier_transform(ft_signal, frequencies, sampled_times):
    ft_real, ft_imag = ft_signal
    n = len(sampled_times)
    reconstructed_signal = np.zeros(n)
    df = frequencies[1] - frequencies[0]  # Frequency step size
    
    for i, t in enumerate(sampled_times):
        # Real part reconstruction using cosine term
        cosine_term = np.cos(2 * np.pi * frequencies * t)
        reconstructed_signal[i] = np.trapz(ft_real * cosine_term - ft_imag * np.sin(2 * np.pi * frequencies * t), frequencies)
    
    return reconstructed_signal

# Reconstruct the signal from the FT data
reconstructed_y_values = inverse_fourier_transform(ft_data, frequencies, sampled_times)

# Plot the original and reconstructed functions for comparison
plt.figure(figsize=(12, 4))
plt.plot(x_values, y_values, label="Original y = x^2", color="blue")
plt.plot(sampled_times, reconstructed_y_values, label="Reconstructed y = x^2", color="red", linestyle="--")
plt.title("Original vs Reconstructed Function (y = x^2)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
