"""
Continuously reads cpu temperature at specified sampling rate. 

On SIGINT singal, before exiting, writes to [filename].csv as follows:

[CPU temperature in celsius], [timestamp]
"""

import temperature as temp
import time
import argparse
import os

def parse_command_line():
    
    # Create Parser
    parser = argparse.ArgumentParser(
                        description = 'Read CPU temperature at rate [RATE] and save to csv in path [DIR].\n Use \'-h\' for more information on parameters.\n')

    # Add Path Argument
    parser.add_argument('-d', metavar='DIR',default='temp_info/temp_info.csv',type=str, help='Path to save results. Must be subdirectory of current path. Saved to temp_info/temp_info.csv by default')
    parser.add_argument('-r', metavar='RATE', default=60, type=int, help="Rate in seconds/sample to read CPU temperature.")

    # Execute parse_args() method
    args = parser.parse_args()
    DIR = args.d # path where results will be saved
    SAMPLING_RATE = args.r # sampling rate of reads

    # Error checking        
    if(DIR.endswith('/')):
        DIR = DIR[:-1]
        
    if(DIR.startswith('/')):
        DIR = DIR[1:]
       
    os.makedirs(os.path.dirname(DIR), exist_ok=True)
    
    return DIR, SAMPLING_RATE

    
DIR, SAMPLING_RATE = parse_command_line()

if(not DIR.endswith(".csv")):
    DIR += ".csv"

while True:
    
    # Read values
    cpu_temp = temp.get_cpu_temp() # cpu temp in C
    timestamp = time.time() # epoch time

    # Append to file
    row = str(cpu_temp) + ',' + str(timestamp) + '\n'
    with open(DIR,'a') as f:
        f.write(row)
    
    # Wait for next sample
    time.sleep(SAMPLING_RATE)
