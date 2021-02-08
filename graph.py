import matplotlib.pyplot as plt
import pandas as pd

sys_info = pd.read_csv('sys_info.csv') 

TEMP_AX_MIN = 20
TEMP_AX_MAX = 35
PWR_AX_MIN = 0
PWR_AX_MAX = 2

CPU_PWR_TEXT_X = 0.15
CPU_PWR_TEXT_Y = 0.95
CPU_TEMP_TEXT_X = 0.15
CPU_TEMP_TEXT_Y = 0.9

GPU_PWR_TEXT_X = 0.15
GPU_PWR_TEXT_Y = 0.95
GPU_TEMP_TEXT_X = 0.15
GPU_TEMP_TEXT_Y = 0.9

# ======= Calculate Averages ====== #
avg_cpu_temp = round(sys_info.cpu_temp.mean(),2)
avg_cpu_pwr = round(sys_info.cpu_pwr.mean(),2)

avg_gpu_temp = round(sys_info.gpu_temp.mean(),2)
avg_gpu_pwr = round(sys_info.gpu_pwr.mean(),2)

# ================= CPU ================= #

fig, ax1 = plt.subplots()
plt.title('CPU Temp/Power',fontsize=20)

# Convert timestamps to minutes elapsed
t_init = sys_info.timestamp[0]
t = list()
for i in sys_info.timestamp:
	t.append((i - t_init)/60)
	
# ====== Averages ====== #
plt.text(CPU_TEMP_TEXT_X,CPU_TEMP_TEXT_Y,('Mean Temp: %s' % avg_cpu_temp),
         horizontalalignment='center',
         verticalalignment='center',
         transform=ax1.transAxes)
         
plt.text(CPU_PWR_TEXT_X,CPU_PWR_TEXT_Y,('Mean Power: %s' % avg_cpu_pwr),
         horizontalalignment='center',
         verticalalignment='center',
         transform=ax1.transAxes)
	
# ======= Temperature ======= #
color = 'tab:blue'
ax1.set_xlabel('Time (min)',fontsize=14)
ax1.set_ylabel('Temperature (C)', color=color,fontsize=14)
ax1.set_ylim([TEMP_AX_MIN,TEMP_AX_MAX])
ax1.plot(t, sys_info.cpu_temp, color=color) # plot CPU temp
ax1.tick_params(axis='y', labelcolor=color)

# ======= Power ======= #
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:red'
ax2.set_ylabel('Power Consumption (W)', color=color,fontsize=14)  # already handled the x-label with ax1
ax2.set_ylim([PWR_AX_MIN,PWR_AX_MAX])
ax2.plot(t, sys_info.cpu_pwr, color=color) # plot CPU power
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped

# save the plot as a file
fig.savefig('cpu_info.jpg',
            format='jpeg',
            dpi=100,
            bbox_inches='tight')
            
# ================= GPU ================= #

fig, ax1 = plt.subplots()
plt.title('GPU Temp/Power',fontsize=20)

# Convert timestamps to minutes elapsed
t_init = sys_info.timestamp[0]
t = list()
for i in sys_info.timestamp:
	t.append((i - t_init)/60)
	
# ====== Averages ====== #
plt.text(GPU_TEMP_TEXT_X,GPU_TEMP_TEXT_Y,('Mean Temp: %s' % avg_gpu_temp),
         horizontalalignment='center',
         verticalalignment='center',
         transform=ax1.transAxes)
         
plt.text(GPU_PWR_TEXT_X,GPU_PWR_TEXT_Y,('Mean Power: %s' % avg_gpu_pwr),
         horizontalalignment='center',
         verticalalignment='center',
         transform=ax1.transAxes)

# ======= Temperature ======= #
color = 'tab:blue'
ax1.set_xlabel('Time (min)',fontsize=14)
ax1.set_ylabel('Temperature (C)', color=color,fontsize=14)
ax1.set_ylim([TEMP_AX_MIN,TEMP_AX_MAX])
ax1.plot(t, sys_info.gpu_temp, color=color) # plot GPU temp
ax1.tick_params(axis='y', labelcolor=color)

# ======= Power ======= #
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:red'
ax2.set_ylabel('Power Consumption (W)', color=color,fontsize=14)  # we already handled the x-label with ax1
ax2.set_ylim([PWR_AX_MIN,PWR_AX_MAX])
ax2.plot(t, sys_info.gpu_pwr, color=color) # plot GPU power
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped

# save the plot as a file
fig.savefig('gpu_info.jpg',
            format='jpeg',
            dpi=100,
            bbox_inches='tight')
