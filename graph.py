import matplotlib.pyplot as plt
import pandas as pd

temp_data = pd.read_csv('temp_data.csv') 
pwr_data = pd.read_csv('pwr_data.csv')

fig, ax1 = plt.subplots()

t_init = temp_data.timestamp[0]
t = list()

for i in temp_data.timestamp:
	t.append((i - t_init)/60)

color = 'tab:red'
ax1.set_xlabel('time (min)')
ax1.set_ylabel('temp (C)', color=color)
ax1.plot(t, temp_data.cpu_temp, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('power consumption (W)', color=color)  # we already handled the x-label with ax1
ax2.plot(t, pwr_data.cpu_pwr, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

# save the plot as a file
fig.savefig('cpu_data.jpg',
            format='jpeg',
            dpi=100,
            bbox_inches='tight')

# data = pd.read_csv('data.csv')
# data.cpu_pwr
# data.cpu_temp
# data.gpu_pwr
# data.gpu_temp