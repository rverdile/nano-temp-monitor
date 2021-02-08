import matplotlib.pyplot as plt
import pandas as pd

sys_info = pd.read_csv('sys_info.csv') 

# ================= CPU ================= #

fig, ax1 = plt.subplots()
plt.title('CPU Temp/Power',fontsize=20)

# Convert timestamps to minutes elapsed
t_init = sys_info.timestamp[0]
t = list()
for i in sys_info.timestamp:
	t.append((i - t_init)/60)

# ======= Temperature ======= #
color = 'tab:blue'
ax1.set_xlabel('Time (min)',fontsize=14)
ax1.set_ylabel('Temperature (C)', color=color,fontsize=14)
ax1.set_ylim([0,100])
ax1.plot(t, sys_info.cpu_temp, color=color) # plot CPU temp
ax1.tick_params(axis='y', labelcolor=color)

# ======= Power ======= #
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:red'
ax2.set_ylabel('Power Consumption (W)', color=color,fontsize=14)  # already handled the x-label with ax1
ax2.set_ylim([0,20])
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
plt.title('CPU Temp/Power',fontsize=20)

# Convert timestamps to minutes elapsed
t_init = sys_info.timestamp[0]
t = list()
for i in sys_info.timestamp:
	t.append((i - t_init)/60)

# ======= Temperature ======= #
color = 'tab:blue'
ax1.set_xlabel('Time (min)',fontsize=14)
ax1.set_ylabel('Temperature (C)', color=color,fontsize=14)
ax1.set_ylim([0,100])
ax1.plot(t, sys_info.gpu_temp, color=color) # plot GPU temp
ax1.tick_params(axis='y', labelcolor=color)

# ======= Power ======= #
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:red'
ax2.set_ylabel('Power Consumption (W)', color=color,fontsize=14)  # we already handled the x-label with ax1
ax2.set_ylim([0,20])
ax2.plot(t, sys_info.gpu_pwr, color=color) # plot GPU power
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped

# save the plot as a file
fig.savefig('gpu_info.jpg',
            format='jpeg',
            dpi=100,
            bbox_inches='tight')
