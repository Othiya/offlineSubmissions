import numpy as np
import matplotlib.pyplot as plt
n=50
samples = np.arange(n) 
sampling_rate=100
wave_velocity=8000

# # Plot function to display signals with step plot
# def plot(x_values, y_values, title="Signal", xlabel="x", ylabel="y"):
#     plt.figure(figsize=(12, 4))
#     plt.step(x_values, y_values, where='mid', label="Signal")  # Using step plot for discrete points
#     plt.title(title)
#     plt.xlabel(xlabel)
#     plt.ylabel(ylabel)
#     plt.legend()
#     plt.grid(True)
#     plt.show()


def plot(
        samples, 
        y_values, 
        title=None,
        x_label='n (Time Index)',
        y_label='x[n]',
    ):
    plt.figure(figsize=(10, 10))
    
    # Set x-ticks to be the same as the sample points (discrete)
    plt.xticks(samples)
     
    y_range = (np.min(y_values)-1,np.max(y_values)+1)
    #y_range=(-2,2) 
    # Adjust y-range dynamically based on the actual signal values in samples
    #y_range = (y_range[0], max(np.max(samples), y_range[1]) + 1)
    
    # Set y-axis limits
    plt.ylim(*y_range)
    
    # Create stem plot: x values are the sample points, and y values are the signal values
    plt.stem(samples, y_values, basefmt=" ")
    
    # Set the plot title, labels, and grid
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    
    plt.show()




#use this function to generate signal_A and signal_B with a random shift
def generate_signals(frequency=5):

    noise_freqs = [15, 30, 45]  # Default noise frequencies in Hz

    amplitudes = [0.5, 0.3, 0.1]  # Default noise amplitudes
    noise_freqs2 = [10, 20, 40] 
    amplitudes2 = [0.3, 0.2, 0.1]
    
     # Discrete sample indices
    dt = 1 / sampling_rate  # Sampling interval in seconds
    time = samples * dt  # Time points corresponding to each sample

    # Original clean signal (sinusoidal)
    original_signal = np.sin(2 * np.pi * frequency * time)

    # Adding noise
    noise_for_sigal_A = sum(amplitude * np.sin(2 * np.pi * noise_freq * time)
                for noise_freq, amplitude in zip(noise_freqs, amplitudes))
    noise_for_sigal_B = sum(amplitude * np.sin(2 * np.pi * noise_freq * time)
                for noise_freq, amplitude in zip(noise_freqs2, amplitudes2))
    signal_A = original_signal + noise_for_sigal_A 
    noisy_signal_B = signal_A + noise_for_sigal_B

    # Applying random shift
    shift_samples = np.random.randint(-n // 2, n // 2)  # Random shift
    print(f"Shift Samples: {shift_samples}")
    signal_B = np.roll(noisy_signal_B, shift_samples)


   
    
    return signal_A, signal_B

#implement other functions and logic

# Fourier Transform 
def DFT(signal):
    total_samples = len(signal)
    dft = np.zeros_like(signal,dtype=complex)

    for k in range(total_samples):
        for n in range(total_samples):
            term = signal[n]*np.exp(-2j*np.pi*k*n / total_samples)
            dft[k] += term

       
    return dft


def IDFT(signal):
    total_samples = len(signal)
    idft = np.zeros_like(signal,dtype=complex)

    for n in range(total_samples):
        for k in range(total_samples):
            term = signal[k]*np.exp(2j*np.pi*k*n / total_samples)
            idft[n] += term

    idft /= total_samples        
        
    return idft

def crossRelation(signal_A,signal_B):
    dftA = DFT(signal_A)
    dftB = DFT(signal_B)

    #freq = dftA*np.conj(dftB)
    freq = dftB*np.conj(dftA)
    time = IDFT(freq)
    
    return time


def getSampleLag(time_domain):

    max_index = np.argmax(np.abs(time_domain))
    N= len(time_domain)
    
    if max_index > N // 2:
        max_index = max_index - N
    
    return max_index

def distanceEstimation(signal_A, signal_B):
    time_domain = crossRelation(signal_A, signal_B)
    sample_lag = getSampleLag(time_domain)
    print(f"Sample Lag: {sample_lag}")
    
    # Calculate distance
    distance = abs(sample_lag) * (1 / sampling_rate) * wave_velocity
    return distance

# def apply_filter(signal):
#     freq = np.abs(DFT(signal))
    
#     for i,f in enumerate(freq):
#        if f <= 5:
#            freq[i]=0

#     plot(samples,freq,"f","a") 

#     back = IDFT(freq)  
#     plot(samples,back,"f","a")    


def apply_filter(signal):

    freq_signal = DFT(signal)
       
    abs_value = np.abs(freq_signal)

    #plot(samples,magnitude,"f","a")
    
    
    top_indices = np.argsort(abs_value)[-4:]  # Indices of top 4 frequencies
    
    
    mask = np.zeros_like(freq_signal, dtype=bool)
    mask[top_indices] = True
    
   
    filtered_freq_signal = np.zeros_like(freq_signal, dtype=complex)
    filtered_freq_signal[mask] = freq_signal[mask]

    #plot(samples,np.abs(filtered_freq_signal),"f","a")
    
    # Perform the inverse DFT to get the filtered signal
    filtered_signal = IDFT(filtered_freq_signal)

    plot(samples,filtered_signal,"f","a")
    
    return filtered_signal    


        
# def distanceEstimation(signal_A,signal_B):
#     time = crossRelation(signal_A,signal_B)
#     sample_lag = np.max(np.abs(time))
#     print("SAMPLE LAG")
#     print(sample_lag)
#     distance = sample_lag * (1/sampling_rate) * wave_velocity

#     return distance




# Generate signals and plot them
signal_A, signal_B = generate_signals()

# plot(samples,signal_A,"signal A","f","amplitude")
# plot(samples,np.abs(DFT(signal_A)),"signal A","f","amplitude")
# plot(samples,signal_B,"f","amplitude")
# plot(samples,np.abs(DFT(signal_B)),"signal B","f","amplitude")
# plot(np.arange(-n//2,n//2),crossRelation(signal_A,signal_B),"DFT based cross relation","lag","co-relation")


#plot(samples,(IDFT(DFT(signal_A))),"f","a")
#plot(samples,IDFT(DFT(signal_B)),"f","a")



print("Estimated Distance:")
print(distanceEstimation(signal_A,signal_B))


filtered_A = apply_filter(signal_A); 
filtered_B = apply_filter(signal_B); 
print("Estimated Distance after Filtering:")
print(distanceEstimation(filtered_A,filtered_B))