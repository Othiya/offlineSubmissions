import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple


# Define the global variable
delta = 0.5

def set_delta(value):
    global delta  # Declare that we are using the global variable
    delta = value  # Modify the global variable


class ContinuousSignal:
    
    def __init__(self,func):
         self.function = func
         

    def set_values(self,x):
         self.x = x     
         self.signal = self.function(x)


    def shift_signal(self,shift):

        def shifted_func(t):
             return self.function(t-shift)
        
        shifted_signal = ContinuousSignal(shifted_func)
        shifted_signal.set_values(self.x)
        return shifted_signal
    

    def add(self,other):
          # Add the y values of the signals directly
        self.signal = [self.signal[i] + other.signal[i] for i in range(len(self.signal))]

        return self  # Return self to allow for chaining if needed

    def multiply(self,other):
            multiplied_signal = self.signal*other
            return multiplied_signal
       
    def multiply_const_factor(self,scaler):
        def scaled_func(t):
            return self.function(t) * scaler
            
        scaled_signal = ContinuousSignal(scaled_func)
        scaled_signal.set_values(self.x)
        # Create a new ContinuousSignal instance with the scaled function
        return scaled_signal
    
            # multiplied_signal = self.signal*scaler
            # return multiplied_signal 
    
    def plot(self):
          plt.figure(figsize=(6, 6))  # Width = 4 inches, Height = 3 inches
          # Plot the graph
          plt.plot(self.x, self.signal, label=r'$x(t)$')
          plt.title("Impulse")
          plt.xlabel('x')
          plt.ylabel('y')
          plt.grid(True)
          plt.axhline(0, color='black',linewidth=0.5)
          plt.axvline(0, color='black',linewidth=0.5)
          plt.legend()
          plt.show()


class LTI_Continous:

    def __init__(self,impulse_response):
          self.h = impulse_response
          

    def linear_combination_of_impulses(self, input_signal, delta):
       """
       Decompose the input signal into a linear combination of impulses.
       Returns the impulses and their coefficients.
       """
       impulses = []
       coefficients = []

       x1 = np.arange(-3, 3+delta,delta)
       y = input_signal.function(x1)  # Ensure input_signal has a `function` method
       #print(y)
       
       r = np.arange(-3*(1/delta), 3*(1/delta)+1)

       for i,val in enumerate(r):
           impulse = ContinuousSignal(func2)  # Ensure func2 is defined
           impulse.set_values(input_signal.x)  # Make sure `x` is properly referenced
 
           coefficient = y[i] * delta
           print(f"coefficient: {coefficient}")

           shifted_impulse = impulse.shift_signal(val*delta)
           
           total_impulse = shifted_impulse.multiply_const_factor(coefficient)
           #total_impulse.plot()
        
           print(f"Shifted impulse after multiplying by coefficient:")
           print(f"y-values: {total_impulse.signal}")

           impulses.append(total_impulse)  # Store shifted impulse signal
           coefficients.append(coefficient)

        # Optional: Only plot after the loop for performance reasons
        # If you want to plot after each iteration, this is fine as well
        # Initialize the output signal with the first impulse
       output = impulses[0]
       for im in impulses[1:]:  # Start from the second impulse
            output = output.add(im)

    
       print(output.signal)  
       output.plot()
    # After loop, return impulses and coefficients
       return impulses, coefficients

     

    def output_approx(self, input_signal, delta):
       impulses = []
       coefficients = []
       
       x1 = np.arange(-3, 3+delta,delta)
       y = input_signal.function(x1)  # Ensure input_signal has a `function` method
       #print(y)
       
       r = np.arange(-3*(1/delta), 3*(1/delta)+1)
    #    x1 = np.arange(-3*(1/delta), 3*(1/delta))
    #    y = input_signal.function(x1)  # Ensure input_signal has a `function` method
    

       for i, val in enumerate(r):
           impulse = ContinuousSignal(func3)  # Ensure func2 is defined
           impulse.set_values(input_signal.x)  # Make sure `x` is properly referenced
 
           coefficient = y[i] * delta
           #print(f"coefficient: {coefficient}")

           shifted_impulse = impulse.shift_signal(val * delta)
           total_impulse = shifted_impulse.multiply_const_factor(coefficient)
        
           #print(f"Shifted impulse after multiplying by coefficient:")
           #print(f"y-values: {total_impulse.signal}")

           impulses.append(total_impulse)  # Store shifted impulse signal
           coefficients.append(coefficient)

        # Optional: Only plot after the loop for performance reasons
        # If you want to plot after each iteration, this is fine as well
        # Initialize the output signal with the first impulse
       output = impulses[0]
       for im in impulses[1:]:  # Start from the second impulse
            output = output.add(im)

    
       print(output.signal)  
       output.plot()

       original = ContinuousSignal(func4)  # Ensure func2 is defined
       original.set_values(input_signal.x)

       #original.plot()
    
    
def func1(x):
        
    #y = np.exp(-x)
    y = np.round(np.exp(-x),3)

    for i,val in enumerate(x):
        if val<0:
            y[i] =0         

    return y
    #return np.where(x>=0,np.exp(-1*x),0)



def func2(x):
    
    
    # Define the unit impulse (or pulse) between 0 and 0.5
    return np.where((x >= 0) & (x < delta), 1/delta, 0)


def func3(x):
    
    # Define the unit impulse (or pulse) between 0 and 0.5
    return np.where(x >= 0, 1, 0)


def func4(x):
        
    y = 1 - np.exp(-x)

    for i,val in enumerate(x):
        if val<0:
            y[i] =0 
    print(y)        

    return y   


    

def main():
    
    set_delta(0.5)

    x = np.linspace(-3,3,2000)


    input_signal = ContinuousSignal(func1)
    input_signal.set_values(x)
    #input_signal.plot()

    

    impulse_response = ContinuousSignal(func2)
    impulse_response.set_values(x)
    
   
    LTI_signal = LTI_Continous(impulse_response)
    co_efficients,unit_impulses = LTI_signal.linear_combination_of_impulses(input_signal,delta)
    
    
    
    LTI_signal.output_approx(input_signal,delta)
    


main()               