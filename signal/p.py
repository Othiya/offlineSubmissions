import numpy as np
import matplotlib.pyplot as plt

# Sample signal (for example, a simple sine wave)
n = 50
sampling_rate = 100
samples = np.arange(n)

# Function to compute DFT manually
def compute_dft(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)  # Initialize the frequency domain representation
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
            
    return X

# Function to compute IDFT manually
def compute_idft(X):
    N = len(X)
    x_reconstructed = np.zeros(N, dtype=complex)  # Initialize the reconstructed time domain signal
    for n in range(N):
        for k in range(N):
            x_reconstructed[n] += X[k] * np.exp(2j * np.pi * k * n / N)
    return x_reconstructed / N

# Generate a signal (for example, a sum of sinusoids)
def generate_signals():
    dt = 1 / sampling_rate
    time = samples * dt
    frequency = 5  # Signal frequency in Hz
    original_signal = np.sin(2 * np.pi * frequency * time)
    
    # Add noise
    noise = 0.5 * np.random.normal(size=n)  # Gaussian noise
    noisy_signal = original_signal + noise
    
    return noisy_signal

# Generate signals
signal_A = generate_signals()
signal_B = generate_signals()

# Compute DFT of both signals
X_A = compute_dft(signal_A)
X_B = compute_dft(signal_B)

# Compute IDFT of both DFTs to reconstruct the signals
reconstructed_signal_A = compute_idft(X_A)
reconstructed_signal_B = compute_idft(X_B)

# Plot the original and reconstructed signals for signal A
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(samples, signal_A, label="Original Signal A")
plt.title("Original Signal A")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(samples, np.real(reconstructed_signal_A), label="Reconstructed Signal A", linestyle='dashed')
plt.title("Reconstructed Signal A (from IDFT)")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot the original and reconstructed signals for signal B
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(samples, signal_B, label="Original Signal B")
plt.title("Original Signal B")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(samples, np.real(reconstructed_signal_B), label="Reconstructed Signal B", linestyle='dashed')
plt.title("Reconstructed Signal B (from IDFT)")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()
