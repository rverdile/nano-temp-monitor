import subprocess

"""
Works with Python 3.6, not necessarily with other versions of Python due
to compatbility with the subprocess library
"""

def get_cpu_temp():
    """
    Returns jetson nano CPU thermal zone temperature in celsius
    """

    
    cpu_therm_proc = subprocess.run(['cat','/sys/class/thermal/thermal_zone0/temp'], # write temp of thermal zone to stdout
                                    check=True, # error checking
                                    stdout=subprocess.PIPE, # get stdout
                                    stderr=subprocess.PIPE, # get stderr
                                    universal_newlines=True) # read stdout/stderr as string

    cpu_therm = float(cpu_therm_proc.stdout)/1000 # divide by 1000 to get celsius
    
    return cpu_therm
    
if __name__ == '__main__':
    
    num_reads = 15
    
    for i in range(num_reads):
        print("=== TEST %s ===" % (i+1))
        print("CPU: %s " % get_cpu_temp())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

