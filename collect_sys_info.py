"""
Continuously reads cpu/gpu temperature and power at specified sampling rate. 

On SIGINT singal, before exiting, writes to sys_info.csv as follows:

[CPU power in watts], [GPU power in watts], [CPU temperature in celsius], [GPU temperature in celsius]
"""

import power as pwr
import temperature as temp
import time
import signal
import sys
import pandas as pd
import numpy as np

SAMPLING_RATE = 1 # samples per second
sys_info = np.ones((0,5))

def signal_handler(signal,frame):
    
    # dataframe written to csv
    df = pd.DataFrame({
        'cpu_pwr':sys_info[:,0],
        'gpu_pwr':sys_info[:,1],
        'tot_pwr':sys_info[:,2],
        'cpu_temp':sys_info[:,3],
        'gpu_temp':sys_info[:,4],
        'timestamp':sys_info[:,5],
    })
    
    df.to_csv('sys_info.csv',mode='w')
           
    sys.exit(0)

while True:
    
    # Read values
    cpu_pwr = pwr.get_cpu_pwr() # cpu power in W
    gpu_pwr = pwr.get_gpu_pwr() # gpu power in W
    tot_pwr = pwr.get_tot_pwr() # tot power in W
    cpu_temp = temp.get_cpu_temp() # cpu temp in C
    gpu_temp = temp.get_gpu_temp() # gpu temp in C
    timestamp = time.time() # epoch time

    # Store values
    sys_info = np.vstack((sys_info,np.array([cpu_pwr,gpu_pwr,tot_pwr,cpu_temp,gpu_temp,timestamp])))
    
    # Handle interrupt 
    signal.signal(signal.SIGINT,signal_handler)
    
    # Wait for next sample
    time.sleep(SAMPLING_RATE)
