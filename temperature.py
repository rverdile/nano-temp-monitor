import subprocess

"""
Works with Python 3.6, not necessarily with other versions of Python due
to compatbility with the subprocess library

thermal zones defined in NVIDIA documentation
use "cat /sys/class/thermal/thermal_zone*/type" to see which number to use (0-5)
"""

def get_cpu_temp():
    """
    Returns jetson nano CPU thermal zone temperature in celsius
    """

    
    cpu_therm_proc = subprocess.run(['cat','/sys/class/thermal/thermal_zone1/temp'], # write temp of thermal zone to stdout
                                    check=True, # error checking
                                    stdout=subprocess.PIPE, # get stdout
                                    stderr=subprocess.PIPE, # get stderr
                                    universal_newlines=True) # read stdout/stderr as string

    cpu_therm = float(cpu_therm_proc.stdout)/1000 # divide by 1000 to get celsius
    
    return cpu_therm
    
def get_gpu_temp():
    """
    Returns jetson nano GPU thermal zone temperature in celsius
    """
    
    gpu_therm_proc = subprocess.run(['cat','/sys/class/thermal/thermal_zone2/temp'],
                                    check=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    universal_newlines=True)

    gpu_therm = float(gpu_therm_proc.stdout)/1000
    
    return gpu_therm
    
def get_fanest_temp():
    """
    Returns thermal fan estimate thermal zone temperature in celsius.
    thermal fan estimate is weighted average of gpu and cpu temperature.
    """
    
    fan_therm_proc = subprocess.run(['cat','/sys/class/thermal/thermal_zone5/temp'],
                                    check=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    universal_newlines=True)

    fan_therm = float(fan_therm_proc.stdout)/1000
    
    return fan_therm

    
if __name__ == '__main__':
    
    num_reads = 15
    
    for i in range(num_reads):
        print("=== TEST %s ===" % (i+1))
        print("CPU: %s " % get_cpu_temp())
        print("GPU: %s " % get_gpu_temp())
        print("FAN: %s " % get_fanest_temp())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

