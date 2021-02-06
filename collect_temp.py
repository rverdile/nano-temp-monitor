"""
Continuously reads gpu and cpu temperatures at specified sampling rate. 

On SIGINT singal, before exiting, writes to temp_data.csv as follows:

[CPU temperature in celsius], [GPU temperature in celsius], [epoch time of read]
"""
import temperature as temp
import time
import signal
import sys
import csv

SAMPLING_RATE = 1 # samples per second
temp_vals = list()

def signal_handler(signal,frame):

    with open('temp_data.csv',mode='a') as f:
        writer = csv.writer(f,delimiter=',')
        
        for i in temp_vals:
            writer.writerow(list(i))
            
    sys.exit(0)



while True:
    
    # Read values
    cpu_temp = temp.get_cpu_temp() # cpu temp in C
    gpu_temp = temp.get_gpu_temp() # gpu temp in C
    timestamp = time.time() # epoch time
    
    # Store values
    temp_vals.append((cpu_temp,gpu_temp,timestamp))
    
    # Handle interrupt
    signal.signal(signal.SIGINT,signal_handler)
    
    # Wait for next sample
    time.sleep(SAMPLING_RATE)
