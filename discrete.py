import numpy as np 
import matplotlib.pyplot as plt 
from typing import Tuple




# def plot(
#         signal, 
#         title=None, 
#         y_range=(-1, 3), 
#         figsize = (8, 3),
#         x_label='n (Time Index)',
#         y_label='x[n]',
#         saveTo=None
#     ):
#     plt.figure(figsize=figsize)
#     plt.xticks(np.arange(-INF, INF + 1, 1))
    
#     y_range = (y_range[0], max(np.max(signal), y_range[1]) + 1)
#     # set y range of 
#     plt.ylim(*y_range)
#     plt.stem(np.arange(-INF, INF + 1, 1), signal)
#     plt.title(title)
#     plt.xlabel(x_label)
#     plt.ylabel(y_label)
#     plt.grid(True)
#     if saveTo is not None:
#         plt.savefig(saveTo)
#     # plt.show()

    

class DiscreteSignal:
       
       def __init__(self,INF):
            self.INF = INF
            self.signal = np.zeros(2*self.INF + 1)
            
       def set_values(self,values_of_signal):
            for i,val in enumerate(values_of_signal):
                 self.signal[i] = val
            
       def set_value_at_time(self,time,value):
           self.signal[time] = value

       def shift_signal(self,shift):
           shifted = np.roll(self.signal,shift)
           return shifted

       def add(self,other):
           summed_signal = self.signal + other
           return summed_signal 

       def multiply(self,other):
            multiplied_signal = self.signal*other
            return multiplied_signal
       
       def multiply_const_factor(self,scaler):
            multiplied_signal = self.signal*scaler
            return multiplied_signal

       def plot_signal(self):
            img_root = '.'
            #plot(self.signal, title='Discrete Signal(x[n])', saveTo=f'{img_root}/discreteSignal.png')  


class  LTI_Discrete:
     
    
     def __init__(self,impulse_response):
          self.h = impulse_response  
     
     def linear_combination_of_impulses(self,input_signal):
         
         unit_impulse = DiscreteSignal(input_signal.INF)
         unit_impulse.set_value_at_time(input_signal.INF,1)
         #print(unit_impulse.signal)
         
         co_efficients =[]
         unit_impulses = []
         

         for i,val in enumerate(input_signal.signal):
              co_efficients.append(val)
              #print(val)
              k = i-input_signal.INF
              shifted = unit_impulse.shift_signal(k)
              shifted *= val
              #print(shifted)
              unit_impulses.append(shifted)

         sum = np.zeros(len(input_signal.signal))
          

         for sub in unit_impulses:
               sum += sub    
        
         #print(sum)    

         

         
         return co_efficients,unit_impulses
         
     

     def output(self,input_signal):
          
          subplots = []
          for i,val in enumerate(input_signal.signal):
               copy = self.h
               
               k = i-input_signal.INF
               
               shifted = copy.shift_signal(k)
               #print(f"shifted :{shifted}")
               subplot = (shifted)*val
               #print(subplot)
               subplots.append(subplot)

          sum = np.zeros(len(input_signal.signal))
          

          for sub in subplots:
               sum += sub    
        
          return sum
     


def main():
    input_signal = DiscreteSignal(5)
    input_signal.set_values(np.array([0,0,0,0,0,0.5,2,0,0,0,0]))
    
    impulse_response = DiscreteSignal(5)
    impulse_response.set_values(np.array([0,0,0,0,0,1,1,1,0,0,0]))
    
    LTI_signal = LTI_Discrete(impulse_response)
    co_efficients,unit_impulses = LTI_signal.linear_combination_of_impulses(input_signal)
    
    sum = LTI_signal.output(input_signal)

    print(sum)


main()     