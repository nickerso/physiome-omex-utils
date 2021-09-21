# To reproduce Figure 7 in the associated Physiome paper,
# execute this script from the command line:
#
#   cd [PathToThisFile]
#   [PathToOpenCOR]/pythonshell Figure7.py

import matplotlib

# matplotlib.use('agg')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

import opencor as opencor

# load the reference model
simulation = opencor.open_simulation("HumanSAN_Fabbri_Fantini_Wilders_Severi_2017.sedml")
data = simulation.data()
data.set_ending_point(2.5)
data.set_point_interval(0.001)

simulation.reset(True)

results = np.zeros((25, 2501))

for i in range(0, 1):
    simulation.run()
    ds = simulation.results().data_store()
    results[0] = ds.voi_and_variables()["environment/time"].values()

for i in range(0, 25):
    simulation.run()
    simulation.clear_results()

simulation.run()
ds = simulation.results().data_store()
results[1] = ds.voi_and_variables()["Membrane/V"].values()
results[4] = ds.voi_and_variables()["i_NaK/i_NaK"].values()
results[7] = ds.voi_and_variables()["Membrane/i_tot"].values()
results[10] = ds.voi_and_variables()["i_Ks/i_Ks"].values()
results[13] = ds.voi_and_variables()["i_f/i_f"].values()
results[16] = ds.voi_and_variables()["i_KACh/i_KACh"].values()
results[19] = ds.voi_and_variables()["i_CaL/i_CaL"].values()
results[22] = ds.voi_and_variables()["Ca_intracellular_fluxes/j_up"].values()

simulation.reset(True)

for i in range(0, 14):
    data.constants()["Rate_modulation_experiments/ACh"] = 1e-5
    simulation.run()
    simulation.clear_results()

simulation.run()
ds = simulation.results().data_store()
results[2] = ds.voi_and_variables()["Membrane/V"].values()
results[5] = ds.voi_and_variables()["i_NaK/i_NaK"].values()
results[8] = ds.voi_and_variables()["Membrane/i_tot"].values()
results[11] = ds.voi_and_variables()["i_Ks/i_Ks"].values()
results[14] = ds.voi_and_variables()["i_f/i_f"].values()
results[17] = ds.voi_and_variables()["i_KACh/i_KACh"].values()
results[20] = ds.voi_and_variables()["i_CaL/i_CaL"].values()
results[23] = ds.voi_and_variables()["Ca_intracellular_fluxes/j_up"].values()

simulation.reset(True)
for i in range(0, 13):
    data.constants()["Rate_modulation_experiments/Iso_1_uM"] = 1
    simulation.run()
    simulation.clear_results()

simulation.run()
ds = simulation.results().data_store()
results[3] = ds.voi_and_variables()["Membrane/V"].values()
results[6] = ds.voi_and_variables()["i_NaK/i_NaK"].values()
results[9] = ds.voi_and_variables()["Membrane/i_tot"].values()
results[12] = ds.voi_and_variables()["i_Ks/i_Ks"].values()
results[15] = ds.voi_and_variables()["i_f/i_f"].values()
results[18] = ds.voi_and_variables()["i_KACh/i_KACh"].values()
results[21] = ds.voi_and_variables()["i_CaL/i_CaL"].values()
results[24] = ds.voi_and_variables()["Ca_intracellular_fluxes/j_up"].values()

# define the x and y axis and match the units
X = results[0] * 1000
Y1 = results[1]
Y2 = results[2]
Y3 = results[3]
Y4 = results[4] * 1000 / 57
Y5 = results[5] * 1000 / 57
Y6 = results[6] * 1000 / 57
Y7 = results[7] * 1000 / 57
Y8 = results[8] * 1000 / 57
Y9 = results[9] * 1000 / 57
Y10 = results[10] * 1000 / 57
Y11 = results[11] * 1000 / 57
Y12 = results[12] * 1000 / 57
Y13 = results[13] * 1000 / 57
Y14 = results[14] * 1000 / 57
Y15 = results[15] * 1000 / 57
Y16 = results[16] * 1000 / 57
Y17 = results[17] * 1000 / 57
Y18 = results[18] * 1000 / 57
Y19 = results[19] * 1000 / 57
Y20 = results[20] * 1000 / 57
Y21 = results[21] * 1000 / 57
Y22 = results[22]
Y23 = results[23]
Y24 = results[24]

plt.figure(figsize=(18, 18))
plt.subplot(4, 2, 1)

plt.plot(X, Y1, 'navy', linestyle='-', label='CTRL', linewidth=3)
plt.plot(X, Y2, 'red', linestyle='-', label='10 nM ACh', linewidth=3)
plt.plot(X, Y3, 'green', linestyle='-', label='1 \u03BCM Iso', linewidth=3)


plt.xlim(0, 2470)
plt.xticks(np.arange(0, 2470, 500))
plt.ylim(-100, 50)
plt.yticks(np.arange(-100, 60, 50))

plt.tick_params(axis='both', labelsize=24)
plt.ylabel('V$_m$ (mV)', fontsize=24)
plt.title('A', loc='left', y=1.05, x=-0.06, fontsize='22')
plt.legend(bbox_to_anchor=(0., 0.83, 1, 0.1), loc='best', fontsize=20, ncol=10, mode="expand")

plt.subplot(4, 2, 2)
plt.plot(X, Y4, 'navy', linestyle='-', label='CTRL', linewidth=3)
plt.plot(X, Y5, 'red', linestyle='-', label='10 nM ACh', linewidth=3)
plt.plot(X, Y6, 'green', linestyle='-', label='1 ${mu}$M Iso', linewidth=3)


plt.xlim(0, 2470)
plt.xticks(np.arange(0, 2470, 500))
plt.ylim(0, 0.3)
plt.yticks(np.arange(0, 0.4, 0.1))

plt.tick_params(axis='both', labelsize=24)
plt.ylabel('I$_{NaK}$ (pA/pF)', fontsize=24)
plt.title('E', loc='left', y=1.05, x=-0.06, fontsize='22')

plt.subplot(4, 2, 3)
plt.plot(X, Y7, 'navy', linestyle='-', label='CTRL', linewidth=3)
plt.plot(X, Y8, 'red', linestyle='-', label='10 nM ACh', linewidth=3)
plt.plot(X, Y9, 'green', linestyle='-', label='1 \u03BC M Iso', linewidth=3)


plt.xlim(0, 2470)
plt.xticks(np.arange(0, 2470, 500))
plt.ylim(-15, 5)
plt.yticks(np.arange(-15, 10, 5))

plt.tick_params(axis='both', labelsize=24)
plt.ylabel('I$_{tot}$ (pA/pF)', fontsize=24)
plt.title('B', loc='left', y=1.05, x=-0.06, fontsize='22')

plt.subplot(4, 2, 4)
plt.plot(X, Y10, 'navy', linestyle='-', label='CTRL', linewidth=3)
plt.plot(X, Y11, 'red', linestyle='-', label='10 nM ACh', linewidth=3)
plt.plot(X, Y12, 'green', linestyle='-', label='1 ${mu}$M Iso', linewidth=3)


plt.xlim(0, 2470)
plt.xticks(np.arange(0, 2470, 500))
plt.ylim(-0.2, 0.4)
plt.yticks(np.arange(-0.2, 0.5, 0.2))

plt.tick_params(axis='both', labelsize=24)
plt.ylabel('I$_{Ks}$ (pA/pF)', fontsize=24)
plt.title('F', loc='left', y=1.05, x=-0.06, fontsize='22')

plt.subplot(4, 2, 5)
plt.plot(X, Y13, 'navy', linestyle='-', label='CTRL', linewidth=3)
plt.plot(X, Y14, 'red', linestyle='-', label='10 nM ACh', linewidth=3)
plt.plot(X, Y15, 'green', linestyle='-', label='1 ${mu}$M Iso', linewidth=3)


plt.xlim(0, 2470)
plt.xticks(np.arange(0, 2470, 500))
plt.ylim(-0.05, 0.05)
plt.yticks(np.arange(-0.05, 0.06, 0.05))

plt.tick_params(axis='both', labelsize=24)
plt.ylabel('I$_{f}$ (pA/pF)', fontsize=24)
plt.title('C', loc='left', y=1.05, x=-0.06, fontsize='22')

plt.subplot(4, 2, 6)
plt.plot(X, Y16, 'navy', linestyle='-', label='CTRL', linewidth=3)
plt.plot(X, Y17, 'red', linestyle='-', label='10 nM ACh', linewidth=3)
plt.plot(X, Y18, 'green', linestyle='-', label='1 ${mu}$M Iso', linewidth=3)


plt.xlim(0, 2470)
plt.xticks(np.arange(0, 2470, 500))
plt.ylim(0, 0.2)
plt.yticks(np.arange(0, 0.25, 0.05))

plt.tick_params(axis='both', labelsize=24)
plt.ylabel('I$_{K,ACh}$ (pA/pF)', fontsize=24)
plt.title('G', loc='left', y=1.05, x=-0.06, fontsize='22')

plt.subplot(4, 2, 7)
plt.plot(X, Y19, 'navy', linestyle='-', label='CTRL', linewidth=3)
plt.plot(X, Y20, 'red', linestyle='-', label='10 nM ACh', linewidth=3)
plt.plot(X, Y21, 'green', linestyle='-', label='1 ${mu}$M Iso', linewidth=3)


plt.xlim(0, 2470)
plt.xticks(np.arange(0, 2470, 500))
plt.ylim(-15, 1)
plt.yticks(np.arange(-15, 2, 5))
plt.xlabel('Time (ms)', fontsize=24)
plt.tick_params(axis='both', labelsize=24)
plt.ylabel('I$_{CaL}$ (pA/pF)', fontsize=24)
plt.title('D', loc='left', y=1.05, x=-0.06, fontsize='22')

plt.subplot(4, 2, 8)
plt.plot(X, Y22, 'navy', linestyle='-', label='CTRL', linewidth=3)
plt.plot(X, Y23, 'red', linestyle='-', label='10 nM ACh', linewidth=3)
plt.plot(X, Y24, 'green', linestyle='-', label='1 ${mu}$M Iso', linewidth=3)


plt.xlim(0, 2470)
plt.xticks(np.arange(0, 2470, 500))
plt.ylim(0, 1.5)
plt.yticks(np.arange(0, 1.6, 0.5))
plt.xlabel('Time (ms)', fontsize=24)
plt.tick_params(axis='both', labelsize=24)
plt.ylabel('J$_{up}$ (mM/s)', fontsize=24)
plt.title('H', loc='left', y=1.05, x=-0.06, fontsize='22')

plt.tight_layout(pad=0.8, w_pad=3, h_pad=3)

plt.savefig('Figure7.png')
plt.show()