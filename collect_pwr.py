"""
Continuously reads GPU and CPU power consumption at specified sampling rate. 

On SIGINT singal, before exiting, writes to pwr_data.csv as follows:

[CPU power in watts], [GPU power in watts], [epoch time of read]
"""
import power as pwr
import time
import signal
import sys
import csv

SAMPLING_RATE = 1 # samples per second
pwr_vals = list()

def signal_handler(signal,frame):

    with open('pwr_data.csv',mode='a') as f:
        writer = csv.writer(f,delimiter=',')
        
        for i in pwr_vals:
            writer.writerow(list(i))
            
    sys.exit(0)



while True:
    
    # Read values
    cpu_pwr = pwr.get_cpu_pwr() # cpu temp in C
    gpu_pwr = pwr.get_gpu_pwr() # gpu temp in C
    timestamp = time.time() # epoch time
    
    # Store values
    pwr_vals.append((cpu_pwr,gpu_pwr,timestamp))
    
    # Handle interrupt
    signal.signal(signal.SIGINT,signal_handler)
    
    # Wait for next sample
    time.sleep(SAMPLING_RATE)
