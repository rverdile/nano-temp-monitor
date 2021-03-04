import subprocess

"""
Works with Python 3.6, not necessarily with other versions of Python due
to compatability with the subprocess library

power0 = total consumption
power1 = gpu consumption
power2 = cpu consumption
"""

def get_cpu_pwr():
    """
    Returns current power consumption in watts of jetson nano CPU
    """

    
    cpu_pwr_proc = subprocess.run(['cat','/sys/bus/i2c/drivers/ina3221x/6-0040/iio:device0/in_power2_input'], # write power in mW of cpu to stdout
                                    check=True, # error checking
                                    stdout=subprocess.PIPE, # get stdout
                                    stderr=subprocess.PIPE, # get stderr
                                    universal_newlines=True) # read stdout/stderr as string

    cpu_pwr = float(cpu_pwr_proc.stdout)/1000 # divide by 1000 to get watts
    
    return cpu_pwr
    
def get_gpu_pwr():
    """
    Returns current power consumption in watts of jetson nano GPU
    """
    
    gpu_pwr_proc = subprocess.run(['cat','/sys/bus/i2c/drivers/ina3221x/6-0040/iio:device0/in_power1_input'],
                                    check=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    universal_newlines=True)

    gpu_pwr = float(gpu_pwr_proc.stdout)/1000
    
    return gpu_pwr
    
def get_total_pwr():
    """
    Returns current total power consumption of jetson nano
    """
    tot_pwr_proc = subprocess.run(['cat','/sys/bus/i2c/drivers/ina3221x/6-0040/iio:device0/in_power0_input'],
                                    check=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    universal_newlines=True)

    tot_pwr = float(tot_pwr_proc.stdout)/1000
    
    return tot_pwr
    
if __name__ == '__main__':
    
    num_reads = 15
    
    for i in range(num_reads):
        print("=== TEST %s ===" % (i+1))
        print("CPU: %s " % get_cpu_pwr())
        print("GPU: %s " % get_gpu_pwr())
        print("TOTAL: %s " % get_total_pwr())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

