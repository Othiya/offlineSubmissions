import numpy as np
import matplotlib.pyplot as plt

class FourierSeries:
    def __init__(self, func, L, terms=10):
        self.func = func
        self.L = L
        self.terms = terms
        self.a0 = self.calculate_a0()
        self.an = [self.calculate_an(n) for n in range(1, terms + 1)]
        self.bn = [self.calculate_bn(n) for n in range(1, terms + 1)]

    def calculate_a0(self, N=1000):
        x = np.linspace(-self.L, self.L, N)
        integral = np.trapz(self.func(x), x)
        return integral / (2 * self.L)

    def calculate_an(self, n, N=1000):
        x = np.linspace(-self.L, self.L, N)
        integral = np.trapz(self.func(x) * np.cos(n * np.pi * x / self.L), x)
        return integral / self.L

    def calculate_bn(self, n, N=1000):
        x = np.linspace(-self.L, self.L, N)
        integral = np.trapz(self.func(x) * np.sin(n * np.pi * x / self.L), x)
        return integral / self.L

    def approximate(self, x):
        series = self.a0
        for n in range(1, self.terms + 1):
            series += self.an[n-1] * np.cos(n * np.pi * x / self.L) + self.bn[n-1] * np.sin(n * np.pi * x / self.L)
        return series

    def plot(self):
        x = np.linspace(-self.L, self.L, 1000)
        original = self.func(x)
        approximation = self.approximate(x)

        plt.figure(figsize=(10, 6))
        plt.plot(x, original, label="Original Function", color="blue")
        plt.plot(x, approximation, label=f"Fourier Series Approximation (N={self.terms})", color="red", linestyle="--")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.title("Fourier Series Approximation")
        plt.grid(True)
        plt.show()


def target_function(x, function_type="square"):
    if function_type == "square":
        return np.sign(np.sin(x))  # Square wave
    elif function_type == "sawtooth":
        return (2 / np.pi) * (x + np.pi) % (2 * np.pi) - 1  # Sawtooth wave
    elif function_type == "triangle":
        return (2 / np.pi) * np.arcsin(np.sin(x))  # Triangle wave
    elif function_type == "sine":
        return np.sin(x)  # Sine wave
    elif function_type == "cosine":
        return np.cos(x)  # Cosine wave
    else:
        raise ValueError("Invalid function_type. Choose from 'square', 'sawtooth', 'triangle', 'sine', or 'cosine'.")


if __name__ == "__main__":
    L = np.pi  # Half-period for all functions
    terms = 10  # Number of terms in Fourier series

    for function_type in ["square", "sawtooth", "triangle", "sine", "cosine"]:
        print(f"Plotting Fourier series for {function_type} wave:")
        
        fourier_series = FourierSeries(lambda x: target_function(x, function_type=function_type), L, terms)
        
        fourier_series.plot()
