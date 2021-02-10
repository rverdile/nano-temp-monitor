import matplotlib.pyplot as plt
import pandas as pd

sys_info = pd.read_csv('sys_info.csv') 

TEMP_AX_MIN = 0
TEMP_AX_MAX = 60
PWR_AX_MIN = 0
PWR_AX_MAX = 10

CPU_PWR_TEXT_X = 0.15
CPU_PWR_TEXT_Y = 0.98
CPU_TEMP_TEXT_X = 0.15
CPU_TEMP_TEXT_Y = 0.98

GPU_PWR_TEXT_X = 0.15
GPU_PWR_TEXT_Y = 0.98
GPU_TEMP_TEXT_X = 0.15
GPU_TEMP_TEXT_Y = 0.98

TITLE_TEXT_SIZE = 30
OTHER_TEXT_SIZE = 20

# ======= Calculate Averages ====== #
avg_cpu_temp = round(sys_info.cpu_temp.mean(),2)
avg_cpu_pwr = round(sys_info.cpu_pwr.mean(),2)

avg_gpu_temp = round(sys_info.gpu_temp.mean(),2)
avg_gpu_pwr = round(sys_info.gpu_pwr.mean(),2)

# ================= CPU ================= #

fig, ax = plt.subplots(1,2,figsize=(20,10))
plt.rc('font',size=12)

# Convert timestamps to minutes elapsed
t_init = sys_info.timestamp[0]
t = list()
for i in sys_info.timestamp:
	t.append((i - t_init)/60)
	
# ====== Averages ====== #
plt.text(CPU_TEMP_TEXT_X,CPU_TEMP_TEXT_Y,('Mean Temp: %s C' % avg_cpu_temp),
         horizontalalignment='center',
         verticalalignment='center',
         fontsize=OTHER_TEXT_SIZE,
         transform=ax[0].transAxes)
         
plt.text(CPU_PWR_TEXT_X,CPU_PWR_TEXT_Y,('Mean Power: %s W' % avg_cpu_pwr),
         horizontalalignment='center',
         verticalalignment='center',
         fontsize=OTHER_TEXT_SIZE,
         transform=ax[1].transAxes)
	
# ======= Temperature ======= #
ax[0].set_title('CPU Temperature',fontsize=TITLE_TEXT_SIZE)
color = 'tab:blue'
ax[0].set_xlabel('Time (min)',fontsize=OTHER_TEXT_SIZE)
ax[0].set_ylabel('Temperature (C)', color=color,fontsize=OTHER_TEXT_SIZE)
ax[0].set_ylim([TEMP_AX_MIN,TEMP_AX_MAX])
ax[0].plot(t, sys_info.cpu_temp, color=color) # plot CPU temp
ax[0].tick_params(axis='y', labelcolor=color)

# ======= Power ======= #
ax[1].set_title('CPU Power',fontsize=TITLE_TEXT_SIZE)
color = 'tab:red'
ax[1].set_xlabel('Time (min)',fontsize=OTHER_TEXT_SIZE)
ax[1].set_ylabel('Power Consumption (W)', color=color,fontsize=OTHER_TEXT_SIZE)
ax[1].set_ylim([PWR_AX_MIN,PWR_AX_MAX])
ax[1].plot(t, sys_info.cpu_pwr, color=color) # plot CPU temp
ax[1].tick_params(axis='y', labelcolor=color)

fig.tight_layout()

# save the plot as a file
fig.savefig('cpu_info.jpg',
            format='jpeg',
            dpi=100,
            bbox_inches='tight')
            
# ================= GPU ================= #

fig, ax = plt.subplots(1,2,figsize=(20,10))
plt.title('GPU Temp/Power',fontsize=20)
plt.rc('font',size=12)

# Convert timestamps to minutes elapsed
t_init = sys_info.timestamp[0]
t = list()
for i in sys_info.timestamp:
	t.append((i - t_init)/60)
	
# ====== Averages ====== #
plt.text(GPU_TEMP_TEXT_X,GPU_TEMP_TEXT_Y,('Mean Temp: %s C' % avg_gpu_temp),
         horizontalalignment='center',
         verticalalignment='center',
         fontsize=OTHER_TEXT_SIZE,
         transform=ax[0].transAxes)
         
plt.text(GPU_PWR_TEXT_X,GPU_PWR_TEXT_Y,('Mean Power: %s W' % avg_gpu_pwr),
         horizontalalignment='center',
         verticalalignment='center',
         fontsize=OTHER_TEXT_SIZE,
         transform=ax[1].transAxes)

# ======= Temperature ======= #
ax[0].set_title('GPU Temperature',fontsize=TITLE_TEXT_SIZE)
color = 'tab:blue'
ax[0].set_xlabel('Time (min)',fontsize=OTHER_TEXT_SIZE)
ax[0].set_ylabel('Temperature (C)', color=color,fontsize=OTHER_TEXT_SIZE)
ax[0].set_ylim([TEMP_AX_MIN,TEMP_AX_MAX])
ax[0].plot(t, sys_info.gpu_temp, color=color) # plot GPU temp
ax[0].tick_params(axis='y', labelcolor=color)

# ======= Power ======= #
ax[1].set_title('GPU Power',fontsize=TITLE_TEXT_SIZE)
color = 'tab:red'
ax[1].set_xlabel('Time (min)',fontsize=OTHER_TEXT_SIZE)
ax[1].set_ylabel('Power Consumption (W)', color=color,fontsize=OTHER_TEXT_SIZE)
ax[1].set_ylim([PWR_AX_MIN,PWR_AX_MAX])
ax[1].plot(t, sys_info.gpu_pwr, color=color) # plot CPU temp
ax[1].tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped

# save the plot as a file
fig.savefig('gpu_info.jpg',
            format='jpeg',
            dpi=100,
            bbox_inches='tight')
