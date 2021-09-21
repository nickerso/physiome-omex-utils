# To reproduce Figure 4 in the associated Physiome paper,
# execute this script from the command line:
#
#   cd [PathToThisFile]
#   [PathToOpenCOR]/pythonshell Figure4.py

import matplotlib

# matplotlib.use('agg')

import numpy as np
import matplotlib.pyplot as plt

import opencor as opencor

# different values for gf to decrease the If
g_f_1 = [0.00427, 0.002989, 0.001281, 0.000427, 0]
t = ["time"]
V_m = {}

# load the reference model
simulation = opencor.open_simulation("Figure4.sedml")
data = simulation.data()
data.set_ending_point(1.9)
data.set_point_interval(0.001)

for gf in g_f_1:
    # reset everything in case we are running interactively and have existing results
    simulation.reset(True)
    simulation.clear_results()

    data.constants()["i_f/g_f_1"] = gf
    simulation.run()
    ds = simulation.results().data_store()
    V_m[gf] = ds.voi_and_variables()["Membrane/V"].values()

simulation.reset(True)
simulation.clear_results()

Time = {}
for i in range(0, 1):
    simulation.run()
    ds = simulation.results().data_store()
    Time[t[0]] = ds.voi_and_variables()["environment/time"].values()

V_m.update(Time)

# define the x and y axis and match the units
X = V_m['time'] * 1000

Y1 = V_m[g_f_1[0]]
Y2 = V_m[g_f_1[1]]
Y3 = V_m[g_f_1[2]]
Y4 = V_m[g_f_1[3]]
Y5 = V_m[g_f_1[4]]

plt.figure(figsize=(14, 12))

plt.plot(X, Y1, 'navy', linestyle='-', label='Control', linewidth=3)
plt.plot(X, Y2, 'red', linestyle='-', label='Block 30%', linewidth=3)
plt.plot(X, Y3, 'green', linestyle='-', label='Block 70%', linewidth=3)
plt.plot(X, Y4, 'purple', linestyle='-', label='Block 90%', linewidth=3)
plt.plot(X, Y5, 'black', linestyle='-', label='Block 100%', linewidth=3)


plt.xlim(0, 1900)
plt.ylim(-60, 30)
plt.xticks(np.arange(0, 1900, 200))
plt.yticks(np.arange(-60, 35, 10))
plt.xlabel('Time (ms)', fontsize=24)
plt.ylabel('V$_m$ (mV)', fontsize=24)

plt.tick_params(axis='x', labelsize=24)
plt.tick_params(axis='y', labelsize=24)

plt.legend(bbox_to_anchor=(0.3, 0.9, 0.25, 0.09), loc='best', fontsize=22,
           ncol=1, mode="expand", borderaxespad=0.)

plt.tight_layout(pad=0.5, w_pad=3, h_pad=3)

plt.savefig('Figure4.png')
plt.show()