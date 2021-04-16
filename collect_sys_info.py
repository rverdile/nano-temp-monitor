"""
Continuously reads cpu temperature at specified sampling rate. 

On SIGINT singal, before exiting, writes to sys_info.csv as follows:

[CPU temperature in celsius], [timestamp]
"""

import temperature as temp
import time
import signal
import sys
import pandas as pd
import numpy as np

SAMPLING_RATE = 1 # samples per second
sys_info = np.ones((0,2))

def signal_handler(signal,frame):
    
    # dataframe written to csv
    df = pd.DataFrame({
        'cpu_temp':sys_info[:,0],
        'timestamp':sys_info[:,1],
    })
    
    df.to_csv('sys_info.csv',mode='w')
           
    sys.exit(0)

while True:
    
    # Read values
    cpu_temp = temp.get_cpu_temp() # cpu temp in C
    timestamp = time.time() # epoch time

    # Store values
    sys_info = np.vstack((sys_info,np.array([cpu_temp,timestamp])))

    
    # Handle interrupt 
    signal.signal(signal.SIGINT,signal_handler)
    
    # Wait for next sample
    time.sleep(SAMPLING_RATE)
