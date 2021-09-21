# To reproduce Figure 1 in the associated Physiome paper,
# execute this script from the command line:
#
#   cd [PathToThisFile]
#   [PathToOpenCOR]/pythonshell Figure1.py

import matplotlib

matplotlib.use('agg')

import numpy as np
import matplotlib.pyplot as plt

import opencor as opencor

# load the reference model
simulation = opencor.open_simulation("HumanSAN_Fabbri_Fantini_Wilders_Severi_2017.sedml")
data = simulation.data()
data.set_ending_point(1.6)
data.set_point_interval(0.001)

results = dict()

simulation.reset(True)
for i in range(29):
    simulation.run()
    simulation.clear_results()

simulation.run()
ds = simulation.results().data_store()
results[0] = ds.voi_and_variables()["environment/time"].values()
results[1] = ds.voi_and_variables()["Membrane/V_ode"].values()
results[2] = ds.voi_and_variables()["Ca_dynamics/Cai"].values()

# define the x and y axis and match the units
X = results[0] * 1000
Y1 = results[1]
Y2 = results[2] * 1e6

plt.figure(figsize=(11, 8))

plt.subplot(2, 1, 1)
plt.plot(X, Y1, 'navy', linestyle='-', label='', linewidth=3)

plt.xlim(0, 1600, 1000)
plt.yticks(np.arange(-70, 40, 20))
plt.ylabel('V$_m$ (mV)', fontsize=22)
plt.tick_params(axis='x', labelsize=18)
plt.tick_params(axis='y', labelsize=18)

plt.title('A', loc='left', y=1.05, x=-0.06, fontsize=22)

plt.tight_layout()

plt.subplot(2, 1, 2)
plt.plot(X, Y2, 'navy', linestyle='-', label='', linewidth=3)

plt.xlim(0, 1600, 1000)
plt.yticks(np.arange(50, 300, 50))
plt.ylabel('[Ca$^{2+}$]$_i$ (nM)', fontsize=22)
plt.xlabel('Time (ms)', fontsize=22)
plt.title('B', loc='left', y=1.05, x=-0.06, fontsize=22)
plt.tick_params(axis='x', labelsize=18)
plt.tick_params(axis='y', labelsize=18)

plt.subplots_adjust(bottom=0.5, right=0.8, top=1)
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

plt.savefig('Figure1.png')

