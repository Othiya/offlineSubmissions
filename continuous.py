import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple
import math


delta = 0.5

def set_delta(value):
    global delta  
    delta = value  #





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
          #  y values of the signals directly
        self.signal = [self.signal[i] + other.signal[i] for i in range(len(self.signal))]

        return self  # Return self to allow for chaining if needed

    def multiply(self,other):
           #  y values of the signals directly
        self.signal = [self.signal[i] * other.signal[i] for i in range(len(self.signal))]

        return self  
       
    def multiply_const_factor(self,scaler):
        def scaled_func(t):
            return self.function(t) * scaler
            
        scaled_signal = ContinuousSignal(scaled_func)
        scaled_signal.set_values(self.x)
        
        return scaled_signal
    
           
    def plot(self,saveTo=None):
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
         
          plt.savefig(saveTo)
          if saveTo is not None:
            plt.savefig(saveTo)
          plt.show()  

    def plotTwo(self,other,saveTo=None):
        # Plot original and shifted signals
        plt.figure()
        plt.plot(self.x, self.signal, label='Original Signal', linestyle='--')
        plt.plot(other.x, other.signal, label=f'constructed Signal', color='red')
        plt.title('Original and Constructed Signal')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.legend()
        plt.grid(True)
        
        plt.savefig(saveTo)
        if saveTo is not None:
           plt.savefig(saveTo)
        plt.show()   

    def subplots(self,impulses, plots_per_row=3,saveTo=None):
       # grid size based on the number of impulses and plots per row
       n_impulses = len(impulses)
       n_rows = math.ceil(n_impulses / plots_per_row)
    
  
       x_min = min(min(impulse.x) for impulse in impulses)
       x_max = max(max(impulse.x) for impulse in impulses)
       y_min = min(min(impulse.signal) for impulse in impulses)
       y_max=1.1
       #y_max = max(max(impulse.signal) for impulse in impulses)
    
    # a figure and a grid of subplots
       fig, axs = plt.subplots(n_rows, plots_per_row, figsize=(12, n_rows * 2.5))
       axs = axs.flatten()  # Flatten in case we don’t have a perfect grid


       for i, total_impulse in enumerate(impulses):
          ax = axs[i]
          ax.plot(total_impulse.x, total_impulse.signal)
        #ax.set_title(f"Total Impulse {i + 1}", fontsize=10)
          ax.set_xlabel("Time", fontsize=8)
          ax.set_ylabel("Amplitude", fontsize=8)
          ax.grid(True)
         
          ax.set_xlim(x_min, x_max)
          ax.set_ylim(y_min, y_max)

       for j in range(i + 1, len(axs)):
          axs[j].axis('off')

    
       plt.tight_layout()
       fig.subplots_adjust(hspace=0.4, wspace=0.4)  # Control spacing
       
       plt.savefig(saveTo)
       if saveTo is not None:
          plt.savefig(saveTo)

       plt.show()

       
    

class LTI_Continous:

    def __init__(self,impulse_response,INF):
          self.h = impulse_response
          self.INF = INF
          

    def linear_combination_of_impulses(self, input_signal, delta):
       """
       Decompose the input signal into a linear combination of impulses.
       Returns the impulses and their coefficients.
       """
       impulses = []
       coefficients = []

       x1 = np.arange(-self.INF, self.INF+delta,delta)
       y = input_signal.function(x1) 
       #print(y)
       
       r = np.arange(-self.INF*(1/delta), self.INF*(1/delta)+1)

       for i,val in enumerate(r):
           impulse = ContinuousSignal(func2)  
           impulse.set_values(input_signal.x)  
 
           coefficient = y[i]
           proper_coefficient = y[i] * delta
           print(f"coefficient: {coefficient}")

           shifted_impulse = impulse.shift_signal(val*delta)
           
           total_impulse = shifted_impulse.multiply_const_factor(proper_coefficient)
           #total_impulse.plot()
        
           print(f"Shifted impulse after multiplying by coefficient:")
           print(f"y-values: {total_impulse.signal}")

           impulses.append(total_impulse)  # shifted impulse signal
           coefficients.append(coefficient)


       input_signal.subplots(impulses,3, saveTo=f'./linearCombinationContinuous.png')

 
       #adding all of them together
       output = impulses[0]
       for im in impulses[1:]:  # from the second impulse
            output = output.add(im)

       input_signal.plotTwo(output,saveTo=f'./VaryingDeltaContinuous.png')

       return impulses, coefficients

     

    def output_approx(self, input_signal, delta):
       impulses = []
       coefficients = []
       
       x1 = np.arange(-self.INF, self.INF+delta,delta)
       y = input_signal.function(x1) 
       #print(y)
       
       r = np.arange(-self.INF*(1/delta), self.INF*(1/delta)+1)
    #    x1 = np.arange(-3*(1/delta), 3*(1/delta))
    #    y = input_signal.function(x1)  # Ensure input_signal has a `function` method
    

       for i, val in enumerate(r):
           impulse = ContinuousSignal(func3) 
           impulse.set_values(input_signal.x)  
 
           coefficient = y[i]
           proper_coefficient = y[i]*delta
           #print(f"coefficient: {coefficient}")

           shifted_impulse = impulse.shift_signal(val * delta)
           total_impulse = shifted_impulse.multiply_const_factor(proper_coefficient)
        
           #print(f"Shifted impulse after multiplying by coefficient:")
           #print(f"y-values: {total_impulse.signal}")

           impulses.append(total_impulse)  # Store shifted impulse signal
           coefficients.append(coefficient)

       input_signal.subplots(impulses,3,saveTo=f'./outputSubplotsContinuous.png')

       output = impulses[0]
       for im in impulses[1:]:  # Start from the second impulse
            output = output.add(im)

    
       actual_output = ContinuousSignal(func4)  # Ensure func2 is defined
       actual_output.set_values(input_signal.x)

       actual_output.plotTwo(output,saveTo=f'./outputContinuous.png')


    
    
def func1(x): 
    #y = np.exp(-x)
    y = np.round(np.exp(-x),3)

    for i,val in enumerate(x):
        if val<0:
            y[i] =0         

    return y


def func2(x):
    # the unit impulse (or pulse) between 0 and 0.5
    return np.where((x >= 0) & (x < delta), 1/delta, 0)


def func3(x): 
    # the unit impulse (or pulse) between 0 and 0.5
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

    x = np.linspace(-3,3,2000) # self.INF=3 in LTI
    input_signal = ContinuousSignal(func1)
    input_signal.set_values(x)
    #input_signal.plot()

    impulse_response = ContinuousSignal(func2)
    impulse_response.set_values(x)
    
    LTI_signal = LTI_Continous(impulse_response,3)
    co_efficients,unit_impulses = LTI_signal.linear_combination_of_impulses(input_signal,delta)
      
    LTI_signal.output_approx(input_signal,delta)


    


main()               