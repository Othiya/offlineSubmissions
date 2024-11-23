import numpy as np
import matplotlib.pyplot as plt


# Parabolic Function: Create a parabolic function y = x2 within the interval [−2,2] and 0 else
# where.
#  • Triangular Function: Create a triangular wave within the interval [−2,2] with height 1 and 0
#  elsewhere.
#  • Sawtooth Function: Create a sawtooth wave within the interval [−2,2] with a slope of 1 and 0
#  elsewhere.
#  • Rectangular Function: Create a rectangular pulse within the interval [−2,2] with a height of 1
#  and 0 elsewhere.

def parabolic(x):
    y = np.where((x>=-2) & (x<=2),x**2,0)
    return y

def rectangle(x):
    y = np.where((x>=-2) & (x<=2),1,0)
    return y

def triangle(x):
    y = np.where((-2 <= x) & (x <= 2), 1 - np.abs(x) / 2, 0)
    return y

def sawtooth(x):
    return np.where((-2 <= x) & (x <= 2), x+2, 0)
    
    # p = 2
    # return np.where((-2 <= x) & (x <= 2), (2 / p) * (x + p) % (2 * p) - 1, 0)
    



# Define the interval and function and generate appropriate x values and y values
x_values = np.linspace(-10,10,1000)
y_values = parabolic(x_values)

# Plot the original function
plt.figure(figsize=(12, 4))
plt.plot(x_values, y_values, label="Original y = x^2")
plt.title("Original Function (y = x^2)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()


# Define the sampled times and frequencies
sampled_times = x_values
frequencies = np.linspace(-2,2,1000)
#frequencies = np.linspace(-1,1,1000)
#frequencies = np.linspace(-5,5,1000)

# Fourier Transform 
def fourier_transform(signal, frequencies, sampled_times):
    num_freqs = len(frequencies)
    ft_result_real = np.zeros(num_freqs)
    ft_result_imag = np.zeros(num_freqs)
    
    # Store the fourier transform results for each frequency. Handle the real and imaginary parts separately
    # use trapezoidal integration to calculate the real and imaginary parts of the FT

    for n,freq in enumerate(frequencies):
        real = np.trapz(signal*np.cos(2*np.pi*freq*sampled_times),sampled_times)
        imaginary = np.trapz(signal*np.sin(2*np.pi*freq*sampled_times),sampled_times)
        ft_result_real[n] = real
        ft_result_imag[n] = imaginary

    return ft_result_real, ft_result_imag

# Apply FT to the sampled data
ft_data = fourier_transform(y_values, frequencies, sampled_times)
print(ft_data)
#  plot the FT data
plt.figure(figsize=(12, 6))
plt.plot(frequencies, np.sqrt(ft_data[0]**2 + ft_data[1]**2))
plt.title("Frequency Spectrum of y = x^2")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()


# Inverse Fourier Transform 
def inverse_fourier_transform(ft_signal, frequencies, sampled_times):
    n = len(sampled_times)
    reconstructed_signal = np.zeros(n)
    # Reconstruct the signal by summing over all frequencies for each time in sampled_times.
    # use trapezoidal integration to calculate the real part
    # You have to return only the real part of the reconstructed signal
    for n,time in enumerate(sampled_times):
        # real = np.trapz(ft_signal[0]*np.cos(2*np.pi*time*frequencies),frequencies)
        # reconstructed_signal[n] = real
        reconstructed_signal[n] = np.trapz(ft_signal[0] * np.cos(2 * np.pi * frequencies * time) + ft_signal[1] * np.sin(2 * np.pi * frequencies * time), frequencies)
    
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
plt.show()
