import numpy as np 
import matplotlib.pyplot as plt 
from typing import Tuple
import math


def plot(signal, INF, saveTo=None):
    # Define y_range based on the signal's minimum and maximum values
    y_min, y_max = np.min(signal.signal), np.max(signal.signal)
    y_range = (y_min, y_max + 1)  # Adjust as needed to ensure full visibility
    
    plt.figure(figsize=(6, 6))
    plt.xticks(np.arange(-INF, INF + 1, 1))
    
    # Set y range based on the calculated y_range
    plt.ylim(*y_range)
    
    # Plot the signal using stem
    plt.stem(np.arange(-INF, INF + 1, 1), signal.signal)
    plt.grid(True)
    
    # Save the figure if a path is provided
    if saveTo is not None:
        plt.savefig(saveTo)
    plt.show()
    


def sub_plots(impulses, INF, plots_per_row=3, saveTo=None):
    
    n_impulses = len(impulses)
    n_rows = math.ceil(n_impulses / plots_per_row)
       
    x_min = -INF
    x_max = INF
    y_min = 0
    y_max = 3  
    
    fig, axs = plt.subplots(n_rows, plots_per_row, figsize=(12, n_rows * 2.5))
    axs = axs.flatten()  

    for i, impulse in enumerate(impulses):
        ax = axs[i]
        ax.set_xticks(np.arange(-INF, INF + 1, 1))
        ax.stem(np.arange(-INF, INF + 1, 1), impulse.signal, basefmt=" ")
        
        # Set labels, grid, and axis limits
        ax.set_xlabel("Time", fontsize=8)
        ax.set_ylabel("Amplitude", fontsize=8)
        ax.grid(True)
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)

    
    for j in range(i + 1, len(axs)):
        axs[j].axis('off')

    
    plt.tight_layout()
    fig.subplots_adjust(hspace=0.4, wspace=0.4) 
    
    
    if saveTo is not None:
        plt.savefig(saveTo)
    plt.show()






class DiscreteSignal:
       
       def __init__(self,INF):
            self.INF = INF
            self.signal = np.zeros(2*self.INF + 1)
            
       def set_values(self,values_of_signal):
            for i,val in enumerate(values_of_signal):
                 self.signal[i] = val
            
       def set_value_at_time(self,time,value):
           self.signal[time + self.INF] = value

       def shift_signal(self,shift):
           shifted = np.roll(self.signal,shift)
           #shifted = np.zeros_like(self.signal)
           n = abs(shift)
           if shift>0:
                shifted[:n] = 0
           elif shift <0:
                shifted[-n:] = 0

           self.signal = shifted     
                
           return self

       def add(self,other):
           self.signal = self.signal + other.signal
           return self 

       def multiply(self,other):
            multiplied_signal = self.signal*other
            return multiplied_signal
       
       def multiply_const_factor(self,scaler):
            self.signal = self.signal*scaler
            return self

        


class  LTI_Discrete:
     
    
     def __init__(self,impulse_response):
          self.h = impulse_response  
     
     def linear_combination_of_impulses(self,input_signal):
         
        
         #print(unit_impulse.signal)
         
         co_efficients =[]
         unit_impulses = []
         

         for i,val in enumerate(input_signal.signal):
              unit_impulse = DiscreteSignal(input_signal.INF)
              unit_impulse.set_value_at_time(0,1)
              
              k = i-input_signal.INF
              shifted = unit_impulse.shift_signal(k)
              
              shifted_multiplied = shifted.multiply_const_factor(val)
              co_efficients.append(val)
              unit_impulses.append(shifted_multiplied)

        
         sum = DiscreteSignal(input_signal.INF)
         sum.set_values(np.zeros(len(input_signal.signal)))
          

         for sub in unit_impulses:
               sum.add(sub)    
        
          
         sub_plots(unit_impulses,input_signal.INF,saveTo=f'./linearCombinationDiscrete.png')
         plot(sum,input_signal.INF,saveTo=f'./linearCombinationSubplotsDiscrete.png')  

         return co_efficients,unit_impulses
         
     

     def output(self,input_signal):
          
          sub_signals = []
          for i,val in enumerate(input_signal.signal):
               copy = DiscreteSignal(self.h.INF)
               copy.set_values(self.h.signal)

               k = i-input_signal.INF
               shifted = copy.shift_signal(k)
               print(f"shifted :{shifted.signal}")
               #sub = (shifted)*val
               shifted_multiplied = shifted.multiply_const_factor(val)
               sub_signals.append(shifted_multiplied)

          sum = DiscreteSignal(input_signal.INF)
          sum.set_values(np.zeros(len(input_signal.signal)))
          

          for sub in sub_signals:
               sum.add(sub)     
          
          sub_plots(sub_signals,input_signal.INF,saveTo=f'./OutputSubplotsDiscrete.png') 
          plot(sum,input_signal.INF,saveTo=f'./OutputDiscrete.png') 
          

          return sum
     


def main():
    input_signal = DiscreteSignal(5)
    input_signal.set_values(np.array([0,0,0,0,0,0.5,2,0,0,0,0]))
    
    impulse_response = DiscreteSignal(5)
    impulse_response.set_values(np.array([0,0,0,0,0,1,1,1,0,0,0]))
    
    LTI_signal = LTI_Discrete(impulse_response)
    co_efficients,unit_impulses = LTI_signal.linear_combination_of_impulses(input_signal)
    
    sum = LTI_signal.output(input_signal)



main()     