# To reproduce Figure 3 in the associated Physiome paper,
# execute this script from the command line:

#   cd [PathToThisFile]
#   [PathToOpenCOR]/pythonshell Figure3.py

import matplotlib

# matplotlib.use('agg')

import matplotlib.pyplot as plt
import opencor as opencor
import numpy as np

# load the reference model
simulation = opencor.open_simulation("HumanSAN_Fabbri_Fantini_Wilders_Severi_2017.sedml")
data = simulation.data()
data.set_ending_point(4.8)
data.set_point_interval(0.001)

simulation.reset(True)

simulation.run()

# cache the reference results
ds = simulation.results().data_store()
variables = ds.voi_and_variables()

# define the x and y axis and match the units
X = variables['environment/time'].values() * 1000
Y1 = variables['Membrane/V'].values()
Y2 = variables['i_CaL/i_CaL'].values() * 1000 / 57
Y3 = variables['i_Na/i_Na'].values() * 1000 / 57
Y4 = variables['i_NaK/i_NaK'].values() * 1000 / 57
Y5 = variables['Membrane/i_tot'].values() * 1000 / 57
Y6 = variables['i_Ks/i_Ks'].values() * 1000 / 57
Y7 = variables['i_Kr/i_Kr'].values() * 1000 / 57
Y8 = variables['i_CaT/i_CaT'].values() * 1000 / 57
Y9 = variables['i_f/i_f'].values() * 1000 / 57
Y10 = variables['i_NaCa/i_NaCa'].values() * 1000 / 57

plt.figure(figsize=(15, 13))

plt.subplot(211)
plt.plot(X, Y1, 'navy', linestyle='-', label='', linewidth=3)

x = np.array([3692, 3800, 3900, 4000, 4100, 4200, 4300, 4400])
values = [" ", "600", "700", "800", "900", "1000", "1100", "1200"]
plt.xlim(3692, 4410)
plt.ylim(-65, -25)
plt.xticks(x, values)
plt.yticks(np.arange(-60, -25, 10))

plt.tick_params(axis='x', labelsize=24)
plt.tick_params(axis='y', labelsize=24)

plt.ylabel('V$_m$ (mV)', fontsize=24)
plt.title('A', loc='left', y=1.05, x=-0.06, fontsize=22)
plt.axvline(x=3745, linewidth=4, label='t$_{MDP}$', color='black')
plt.axvline(x=3845, linewidth=4, label='t$_{MDP}$+100 ms', linestyle='dotted', color='black')
plt.axvline(x=4365, linewidth=4, label='t$_{TOP}$', color='grey')
plt.legend(loc='best', fontsize=22)

plt.subplot(212)
plt.plot(X, Y2, 'navy', linestyle='-', label='I$_{CaL}$', linewidth=3)
plt.plot(X, Y3, 'red', linestyle='-', label='I$_{Na}$', linewidth=3)
plt.plot(X, Y4, 'green', linestyle='-', label='I$_{NaK}$', linewidth=3)
plt.plot(X, Y5, 'black', linestyle='-.', label='I$_{tot}$', linewidth=3)
plt.plot(X, Y6, 'orange', linestyle='-', label='I$_{Ks}$', linewidth=3)
plt.plot(X, Y7, 'purple', linestyle='-', label='I$_{Kr}$', linewidth=3)
plt.plot(X, Y8, 'grey', linestyle='-', label='I$_{CaT}$', linewidth=3)
plt.plot(X, Y9, 'black', linestyle='-', label='I$_{f}$', linewidth=3)
plt.plot(X, Y10, 'blue', linestyle='-', label='I$_{NaCa}$', linewidth=3)


x = np.array([3692, 3800, 3900, 4000, 4100, 4200, 4300, 4400])
values = [" ", "600", "700", "800", "900", "1000", "1100", "1200"]
plt.xlim(3692, 4410)
plt.ylim(-0.15, 0.2)
plt.xticks(x, values)
plt.xlabel('Time (ms)', fontsize=24)
plt.tick_params(axis='x', labelsize=24)
plt.tick_params(axis='y', labelsize=24)

plt.ylabel('(pA/Pf)', fontsize=24)

plt.title('B', loc='left', y=1.05, x=-0.06, fontsize=22)
plt.legend(bbox_to_anchor=(0.15, 0.75, 0.7, 0.04), loc='best', fontsize=26,
           ncol=5, mode="expand", borderaxespad=0.)

plt.tight_layout(pad=0.5, w_pad=3, h_pad=3)

plt.savefig('Figure3.png')
plt.show()

