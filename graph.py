import matplotlib.pyplot as plt
import pandas as pd

sys_info = pd.read_csv('idle_sys_info.csv') 

TEMP_AX_MIN = 0
TEMP_AX_MAX = 50
PWR_AX_MIN = 0
PWR_AX_MAX = 3


CPU_TEMP_TEXT_X = 0.22
CPU_TEMP_TEXT_Y = 0.97
GPU_TEMP_TEXT_X = 0.21
GPU_TEMP_TEXT_Y = 0.97

CPU_PWR_TEXT_X = 0.33
CPU_PWR_TEXT_Y = 0.97
GPU_PWR_TEXT_X = 0.33
GPU_PWR_TEXT_Y = 0.97
TOT_PWR_TEXT_X = 0.33
TOT_PWR_TEXT_Y = 0.97

TITLE_TEXT_SIZE = 30
OTHER_TEXT_SIZE = 20

# ======= Calculate Averages ====== #
avg_cpu_temp = round(sys_info.cpu_temp.mean(),2)
avg_gpu_temp = round(sys_info.gpu_temp.mean(),2)

avg_cpu_pwr = round(sys_info.cpu_pwr.mean(),2)
avg_gpu_pwr = round(sys_info.gpu_pwr.mean(),2)
avg_tot_pwr = round(sys_info.tot_pwr.mean(),2)

# ================= Temperature ================= #

fig, ax = plt.subplots(1,2,figsize=(20,10))
fig.suptitle("Open: Low Activity", fontsize=TITLE_TEXT_SIZE+5)
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
         
plt.text(GPU_TEMP_TEXT_X,GPU_TEMP_TEXT_Y,('Mean Temp: %s C' % avg_gpu_temp),
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
ax[0].scatter(t, sys_info.cpu_temp, color=color) # plot CPU temp
ax[0].tick_params(axis='y', labelcolor=color)

# ======= Power ======= #
ax[1].set_title('GPU Temperature',fontsize=TITLE_TEXT_SIZE)
color = 'tab:red'
ax[1].set_xlabel('Time (min)',fontsize=OTHER_TEXT_SIZE)
ax[1].set_ylabel('Temperature (C)', color=color,fontsize=OTHER_TEXT_SIZE)
ax[1].set_ylim([TEMP_AX_MIN,TEMP_AX_MAX])
ax[1].scatter(t, sys_info.gpu_temp, color=color) # plot GPU temp
ax[1].tick_params(axis='y', labelcolor=color)

# save the plot as a file
fig.savefig('temp_info.jpg',
            format='jpeg',
            dpi=100,
            bbox_inches='tight')
            
# ================= Power ================= #

fig, ax = plt.subplots(1,3,figsize=(20,10))
fig.suptitle("Open: Low Activity", fontsize=TITLE_TEXT_SIZE+5)
plt.rc('font',size=12)

# Convert timestamps to minutes elapsed
t_init = sys_info.timestamp[0]
t = list()
for i in sys_info.timestamp:
	t.append((i - t_init)/60)
	
# ====== Averages ====== #
plt.text(CPU_PWR_TEXT_X,CPU_PWR_TEXT_Y,('Mean Power: %s W' % avg_cpu_pwr),
         horizontalalignment='center',
         verticalalignment='center',
         fontsize=OTHER_TEXT_SIZE,
         transform=ax[0].transAxes)
         
plt.text(GPU_PWR_TEXT_X,GPU_PWR_TEXT_Y,('Mean Power: %s W' % avg_gpu_pwr),
         horizontalalignment='center',
         verticalalignment='center',
         fontsize=OTHER_TEXT_SIZE,
         transform=ax[1].transAxes)

plt.text(TOT_PWR_TEXT_X,TOT_PWR_TEXT_Y,('Mean Power: %s W' % avg_tot_pwr),
         horizontalalignment='center',
         verticalalignment='center',
         fontsize=OTHER_TEXT_SIZE,
         transform=ax[2].transAxes)

# ======= CPU Power ======= #
ax[0].set_title('CPU Power',fontsize=TITLE_TEXT_SIZE)
color = 'tab:blue'
ax[0].set_xlabel('Time (min)',fontsize=OTHER_TEXT_SIZE)
ax[0].set_ylabel('Power Consumption (W)', color=color,fontsize=OTHER_TEXT_SIZE)
ax[0].set_ylim([PWR_AX_MIN,PWR_AX_MAX])
ax[0].scatter(t, sys_info.cpu_pwr, color=color) # plot CPU power
ax[0].tick_params(axis='y', labelcolor=color)

# ======= GPU Power ======= #
ax[1].set_title('GPU Power',fontsize=TITLE_TEXT_SIZE)
color = 'tab:red'
ax[1].set_xlabel('Time (min)',fontsize=OTHER_TEXT_SIZE)
ax[1].set_ylabel('Power Consumption (W)', color=color,fontsize=OTHER_TEXT_SIZE)
ax[1].set_ylim([PWR_AX_MIN,PWR_AX_MAX])
ax[1].scatter(t, sys_info.gpu_pwr, color=color) # plot CPU temp
ax[1].tick_params(axis='y', labelcolor=color)

# ====== Total Power ====== #
ax[2].set_title('Total Power',fontsize=TITLE_TEXT_SIZE)
color = 'tab:green'
ax[2].set_xlabel('Time (min)',fontsize=OTHER_TEXT_SIZE)
ax[2].set_ylabel('Power Consumption (W)', color=color,fontsize=OTHER_TEXT_SIZE)
ax[2].set_ylim([PWR_AX_MIN,PWR_AX_MAX])
ax[2].scatter(t, sys_info.tot_pwr, color=color) # plot CPU temp
ax[2].tick_params(axis='y', labelcolor=color)

# save the plot as a file
fig.savefig('power_info.jpg',
            format='jpeg',
            dpi=100,
            bbox_inches='tight')
