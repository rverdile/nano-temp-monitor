import matplotlib.pyplot as plt
import pandas as pd

sys_info = pd.read_csv('sys_info.csv') 

TEMP_AX_MIN = 0
TEMP_AX_MAX = 70
PWR_AX_MIN = 0
PWR_AX_MAX = 10


CPU_TEMP_TEXT_X = 0.22
CPU_TEMP_TEXT_Y = 0.97

TITLE_TEXT_SIZE = 30
OTHER_TEXT_SIZE = 20

# ======= Calculate Averages ====== #
avg_cpu_temp = round(sys_info.cpu_temp.mean(),2)

# ================= Temperature ================= #

fig, ax = plt.subplots(1,2,figsize=(20,10))
fig.suptitle("RPI CPU Temp", fontsize=TITLE_TEXT_SIZE+5)
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
         
# ======= Temperature ======= #
ax[0].set_title('CPU Temperature',fontsize=TITLE_TEXT_SIZE)
color = 'tab:blue'
ax[0].set_xlabel('Time (min)',fontsize=OTHER_TEXT_SIZE)
ax[0].set_ylabel('Temperature (C)', color=color,fontsize=OTHER_TEXT_SIZE)
ax[0].set_ylim([TEMP_AX_MIN,TEMP_AX_MAX])
ax[0].scatter(t, sys_info.cpu_temp, color=color) # plot CPU temp
ax[0].tick_params(axis='y', labelcolor=color)

# save the plot as a file
fig.savefig('temp_info.jpg',
            format='jpeg',
            dpi=100,
            bbox_inches='tight')
