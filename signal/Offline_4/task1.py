import numpy as np
import matplotlib.pyplot as plt
n=50
samples = np.arange(n) 
sampling_rate=100
wave_velocity=8000

# Plot function to display signals
def plot(x_values, y_values, title="Signal", xlabel="x", ylabel="y"):
    plt.figure(figsize=(12, 4))
    plt.plot(x_values, y_values, label="Signal")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
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

    freq = dftA*np.conj(dftB)
    time = IDFT(freq)

    return time


 


# Generate signals and plot them
signal_A, signal_B = generate_signals()

 # Plot both signals
plot(samples, signal_A, title="Signal A (Original + Noise)")
plot(samples,(IDFT(DFT(signal_A))),"f","a")
plot(samples, signal_B, title="Signal B (Shifted)")
plot(samples,IDFT(DFT(signal_B)),"f","a")

plot(samples,crossRelation(signal_A,signal_B),"cross","relation")