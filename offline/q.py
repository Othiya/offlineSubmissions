import numpy as np
import matplotlib.pyplot as plt

# Define the sawtooth function
def sawtooth_wave(t, p):
    return 2 * (x / (2*np.pi)- np.floor(1/2 + x/(2*np.pi)))

# Create a time array, for example from 0 to 5 with 1000 points
t = np.linspace(0, 5, 1000)

# Define the period
p = 1  # Change this value for a different period

# Calculate the sawtooth wave values
y = sawtooth_wave(t, p)

# Plot the sawtooth wave
plt.plot(t, y)
plt.title("Sawtooth Wave")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
