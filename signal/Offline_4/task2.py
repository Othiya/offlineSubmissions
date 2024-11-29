import numpy as np
import matplotlib.pyplot as plt
import time



def plot(
        samples, 
        y_values, 
        title=None,
        x_label='n (Time Index)',
        y_label='x[n]',
    ):
    plt.figure(figsize=(12, 12))
    
    # Set x-ticks to be the same as the sample points (discrete)
    plt.xticks(samples)
     
    y_range = (np.min(y_values)-1,np.max(y_values)+1)
    # Adjust y-range dynamically based on the actual signal values in samples
    plt.ylim(*y_range)
    
    # Create stem plot: x values are the sample points, and y values are the signal values
    plt.stem(samples, y_values, basefmt=" ")
    
    # Set the plot title, labels, and grid
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    
    plt.show()

def plot1(n_samples,time1,time2,label1,label2,title):
    # Plotting the results
    plt.figure(figsize=(10, 6))

# Plot for DFT/FFT and IDFT/IFFT times
    plt.plot(n_samples, time1, label=label1, marker='o')
    plt.plot(n_samples, time2, label=label2, marker='o')


# Labeling the axes and title
    plt.xlabel('Number of Samples (n)', fontsize=12)
    plt.ylabel('Average Execution Time (seconds)', fontsize=12)
    plt.title(title, fontsize=14)

# Adding grid and legend
    plt.grid(True)
    plt.legend()

# Show the plot
    plt.show()

def FFT(x):
    """
    A recursive implementation of the 1D Cooley-Tukey FFT, the input should have a length of 
    power of 2.
    """
    N = len(x)
    
    if N == 1:
        return x
    else:
        # Split the input into even and odd indexed parts
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        
        # Calculate the factor (complex exponential)
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        
        # # Combine the even and odd parts
        # X = np.zeros(N, dtype=complex)
        
        # # The first half of the result corresponds to X_even + factor[:N//2] * X_odd
        
        # X[:N//2] = X_even + factor[:N//2] * X_odd
        
        # # The second half of the result corresponds to X_even + factor[N//2:] * X_odd
        # X[N//2:] = X_even + factor[N//2:] * X_odd

        X = np.concatenate(
            [X_even + factor[:int(N/2)] * X_odd,
             X_even + factor[int(N/2):] * X_odd])
        
        return X


def IFFT(x):
    """
    A recursive implementation of 
    the 1D Cooley-Tukey IFFT, the 
    input should have a length of 
    power of 2. 
    """
    N = len(x)
    
    if N == 1:
        return x
    else:
        X_even = IFFT(x[::2])
        X_odd = IFFT(x[1::2])
        factor = np.exp(2j * np.pi * np.arange(N) / N)
        
        X = np.concatenate(
            [X_even + factor[:int(N/2)] * X_odd,
             X_even + factor[int(N/2):] * X_odd])
        return X


# Fourier Transform 
def DFT(signal):
    total_samples = len(signal)
    dft = np.zeros_like(signal, dtype=complex)

    for k in range(total_samples):
        for n in range(total_samples):
            term = signal[n] * np.exp(-2j * np.pi * k * n / total_samples)
            dft[k] += term

    return dft


def IDFT(signal):
    total_samples = len(signal)
    idft = np.zeros_like(signal, dtype=complex)

    for n in range(total_samples):
        for k in range(total_samples):
            term = signal[k] * np.exp(2j * np.pi * k * n / total_samples)
            idft[n] += term

    idft /= total_samples        
    return idft

# Sample sizes
n_samples = np.array([2, 4, 8, 16, 32, 64,128,256,512])

# Initialize arrays to store the times for each algorithm
dft_time = np.zeros_like(n_samples, dtype=float)
fft_time = np.zeros_like(n_samples, dtype=float)
idft_time = np.zeros_like(n_samples, dtype=float)
ifft_time = np.zeros_like(n_samples, dtype=float)

# Loop through each sample size
for k, n in enumerate(n_samples):

    samples = np.arange(n) 
    signal = np.array([np.sin(2 * np.pi * k / n) for k in range(n)], dtype=complex)

    # Timing variables
    total_time_dft = 0
    total_time_fft = 0
    total_time_idft = 0
    total_time_ifft = 0

    # Measure the times for DFT, FFT, IDFT, IFFT (run 10 times each)
    for i in range(10):
        # DFT timing
        start_time_dft = time.time()
        result_dft = DFT(signal)
        end_time_dft = time.time()
        total_time_dft += (end_time_dft - start_time_dft)

        # FFT timing
        start_time_fft = time.time()
        result_fft = FFT(signal)
        end_time_fft = time.time()
        total_time_fft += (end_time_fft - start_time_fft)

        # IDFT timing
        start_time_idft = time.time()
        result_idft = IDFT(result_dft)
        end_time_idft = time.time()
        total_time_idft += (end_time_idft - start_time_idft)

        # IFFT timing
        start_time_ifft = time.time()
        result_ifft = IFFT(result_fft)
        end_time_ifft = time.time()
        total_time_ifft += (end_time_ifft - start_time_ifft)
    
    # Store the average times
    dft_time[k] = total_time_dft / 10.0
    fft_time[k] = total_time_fft / 10.0
    idft_time[k] = total_time_idft / 10.0
    ifft_time[k] = total_time_ifft / 10.0




plot1(n_samples,dft_time,fft_time,"DFT","FFT","DFT vs FFT Execution Time Comparison")
plot1(n_samples,idft_time,ifft_time,"IDFT","IFFT","IDFT vs IFFT Execution Time Comparison")
