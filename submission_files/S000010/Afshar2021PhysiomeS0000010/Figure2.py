# To reproduce Figure 2 in the associated Physiome paper,
# execute this script from the command line:
#
#   cd [PathToThisFile]
#   [PathToOpenCOR]/pythonshell Figure2.py

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

for i in range(2):
    simulation.run()
    simulation.clear_results()

simulation.run()
ds = simulation.results().data_store()
results[0] = ds.voi_and_variables()["environment/time"].values()
results[1] = ds.voi_and_variables()["Membrane/V_ode"].values()
results[2] = ds.voi_and_variables()["Membrane/i_tot"].values()
results[3] = ds.voi_and_variables()["Ca_SR_release/j_SRCarel"].values()
results[4] = ds.voi_and_variables()["i_CaL/i_CaL"].values()
results[5] = ds.voi_and_variables()["i_Kr/i_Kr"].values()
results[6] = ds.voi_and_variables()["Ca_intracellular_fluxes/j_up"].values()
results[7] = ds.voi_and_variables()["i_f/i_f"].values()
results[8] = ds.voi_and_variables()["i_Ks/i_Ks"].values()
results[9] = ds.voi_and_variables()["i_Na/i_Na"].values()
results[10] = ds.voi_and_variables()["i_CaT/i_CaT"].values()
results[11] = ds.voi_and_variables()["Ca_dynamics/Ca_sub"].values()
results[12] = ds.voi_and_variables()["i_NaCa/i_NaCa"].values()
results[13] = ds.voi_and_variables()["i_NaK/i_NaK"].values()
results[14] = ds.voi_and_variables()["Ca_dynamics/Cai"].values()
results[15] = ds.voi_and_variables()["i_Kur/i_Kur"].values()
results[16] = ds.voi_and_variables()["i_to/i_to"].values()
results[17] = ds.voi_and_variables()["Ca_dynamics/Ca_jsr"].values()
results[18] = ds.voi_and_variables()["Ca_dynamics/Ca_nsr"].values()

# define the x and y axis and match the units
X = results[0] * 1000
Y1 = results[1]
Y2 = results[2] * 1000 / 57
Y3 = results[3]
Y4 = results[4] * 1000 / 57
Y5 = results[5] * 1000 / 57
Y6 = results[6]
Y7 = results[7] * 1000 / 57
Y8 = results[8] * 1000 / 57
Y9 = results[9] * 1000 / 57
Y10 = results[10] * 1000 / 57
Y11 = results[11] * 1000
Y12 = results[12] * 1000 / 57
Y13 = results[13] * 1000 / 57
Y14 = results[14] * 1e6
Y15 = results[15] * 1000 / 57
Y16 = results[16] * 1000 / 57
Y17 = results[17]
Y18 = results[18]

plt.figure(figsize=(18, 18))

plt.subplot(6, 2, 1)
plt.plot(X, Y1, 'navy', linestyle='-', label='', linewidth=3)

plt.xlim(0, 1600)
plt.xticks(np.arange(0, 1600, 500))
plt.ylim(-70, 30)
plt.yticks(np.arange(-60, 30, 20))
plt.tick_params(axis='x', labelsize=22)
plt.tick_params(axis='y', labelsize=22)
plt.ylabel('V$_m$ (mV)', fontsize=22)

plt.title('A', loc='left', y=1.05, x=-0.06, fontsize=22)


plt.subplot(6, 2, 2)
plt.plot(X, Y1, 'navy', linestyle='-', label='', linewidth=3)

plt.xlim(0, 1600)
plt.xticks(np.arange(0, 1600, 500))
plt.ylim(-70, 30)
plt.yticks(np.arange(-60, 30, 20))
plt.tick_params(axis='x', labelsize=22)
plt.tick_params(axis='y', labelsize=22)
plt.ylabel('V$_m$ (mV)', fontsize=22)


plt.subplot(6, 2, 3)
plt.plot(X, Y2, 'navy', linestyle='-', label='', linewidth=3)

plt.xlim(0, 1600)
plt.xticks(np.arange(0, 1600, 500))
plt.ylim(-8, 3)
plt.yticks(np.arange(-8, 4, 2))
plt.tick_params(axis='x', labelsize=22)
plt.tick_params(axis='y', labelsize=22)
plt.ylabel('I$_{tot}$ (pA/pF)', fontsize=22)
plt.title('B', loc='left', y=1.05, x=-0.06, fontsize=22)


plt.subplot(6, 2, 4)
plt.plot(X, Y3, 'navy', linestyle='-', label='', linewidth=3)

plt.xlim(0, 1600)
plt.xticks(np.arange(0, 1600, 500))
plt.yticks(np.arange(0, 310, 100))
plt.tick_params(axis='x', labelsize=22)
plt.tick_params(axis='y', labelsize=22)
plt.ylabel('J$_{rel}$ (mM/s)', fontsize=22)

plt.title('G', loc='left', y=1.05, x=-0.06, fontsize=22)

plt.subplot(6, 2, 5)
plt.plot(X, Y4, 'navy', linestyle='-', label='I$_{CaL}$', linewidth=3)
plt.plot(X, Y5, 'red', linestyle='-', label='I$_{Kr}$', linewidth=3)
plt.tick_params(axis='x', labelsize=22)
plt.tick_params(axis='y', labelsize=22)
plt.xlim(0, 1600)
plt.xticks(np.arange(0, 1600, 500))
plt.ylim(-8, 3)
plt.yticks(np.arange(-8, 3, 2))
plt.ylabel('(pA/pF)', fontsize=22)

plt.title('C', loc='left', y=1.05, x=-0.06, fontsize=22)


plt.legend(fontsize= 20)

plt.subplot(6, 2, 6)
plt.plot(X, Y6, 'navy', linestyle='-', label='I$_{CaL}$', linewidth=3)
plt.tick_params(axis='x', labelsize=22)
plt.tick_params(axis='y', labelsize=22)
plt.xlim(0, 1600)
plt.xticks(np.arange(0, 1600, 500))
plt.yticks(np.arange(0, 1, 0.2))
plt.ylabel('J$_{up}$ (mM/s)', fontsize=22)

plt.title('H', loc='left', y=1.05, x=-0.06, fontsize=22)


plt.subplot(6, 2, 7)
plt.plot(X, Y7, 'navy', linestyle='-', label='I$_{f}$', linewidth=3)
plt.plot(X, Y8, 'red', linestyle='-', label='I$_{Ks}$', linewidth=3)
plt.plot(X, Y9, 'green', linestyle='-', label='I$_{Na}$', linewidth=3)
plt.plot(X, Y10, 'purple', linestyle='-', label='I$_{CaT}$', linewidth=3)
plt.tick_params(axis='x', labelsize=22)
plt.tick_params(axis='y', labelsize=22)
plt.xlim(0, 1600)
plt.xticks(np.arange(0, 1600, 500))
plt.ylim(-0.1, 0.051)
plt.yticks(np.arange(-0.1, 0.051, 0.05))
plt.ylabel('(pA/pF)', fontsize=22)
plt.title('D', loc='left', y=1.05, x=-0.06, fontsize=22)


plt.legend(bbox_to_anchor=(0.1, 0.2, 0.8, 0.05), loc='best', fontsize=20,
           ncol=5, mode="expand", borderaxespad=0.)

plt.subplot(6, 2, 8)
plt.plot(X, Y11, 'navy', linestyle='-', label='I$_{CaL}$', linewidth=3)

plt.xlim(0, 1600)
plt.xticks(np.arange(0, 1600, 500))
plt.yticks(np.arange(0, 3.1, 1))
plt.tick_params(axis='x', labelsize=22)
plt.tick_params(axis='y', labelsize=22)
plt.ylabel('Ca$_{sub}$ (\u03BCM)', fontsize=22)
plt.title('I', loc='left', y=1.05, x=-0.06, fontsize=22)


plt.subplot(6, 2, 9)
plt.plot(X, Y12, 'navy', linestyle='-', label='I$_{NaCa}$', linewidth=3)
plt.plot(X, Y13, 'red', linestyle='-', label='I$_{NaK}$', linewidth=3)
plt.tick_params(axis='x', labelsize=22)
plt.tick_params(axis='y', labelsize=22)
plt.xlim(0, 1600, 1000)
plt.xticks(np.arange(0, 1700, 500))
plt.yticks(np.arange(-2, 1, 0.5))
plt.ylabel('(pA/pF)', fontsize=22)
plt.title('E', loc='left', y=1.05, x=-0.06, fontsize=22)


plt.legend(fontsize= 20)

plt.subplot(6, 2, 10)
plt.plot(X, Y14, 'navy', linestyle='-', label='I$_{CaL}$', linewidth=3)

plt.xlim(0, 1600)
plt.xticks(np.arange(0, 1600, 500))
plt.yticks(np.arange(50, 250, 50))
plt.ylabel('Ca$_i$ (nM)', fontsize=22)
plt.title('J', loc='left', y=1.07, x=-0.06, fontsize=22)
plt.tick_params(axis='x', labelsize=22)
plt.tick_params(axis='y', labelsize=22)
plt.subplots_adjust(bottom=0.5, right=0.8, top=1)

plt.subplot(6, 2, 11)
plt.plot(X, Y15, 'navy', linestyle='-', label='$I_{Kur}$', linewidth=3)
plt.plot(X, Y16, 'red', linestyle='-', label='$I_{to}$', linewidth=3)

plt.xlim(0, 1600)
plt.xticks(np.arange(0, 1600, 500))
plt.yticks(np.arange(0, 0.5, 0.1))
plt.ylabel('(pA/pF)', fontsize=22)
plt.xlabel('Time (ms)', fontsize=22)
plt.title('F', loc='left', y=1.05, x=-0.06, fontsize=22)
plt.tick_params(axis='x', labelsize=22)
plt.tick_params(axis='y', labelsize=22)
plt.subplots_adjust(bottom=0.5, right=0.8, top=1)

plt.legend(fontsize= 20)

plt.subplot(6, 2, 12)
plt.plot(X, Y17, 'navy', linestyle='-', label='$Ca_{jSR}$', linewidth=3)
plt.plot(X, Y18, 'red', linestyle='-', label='$Ca_{nSR}$', linewidth=3)

plt.xlim(0, 1600)
plt.xticks(np.arange(0, 1600, 500))
plt.yticks(np.arange(0.1, 0.6, 0.1))
plt.ylabel('(mM)', fontsize=22)
plt.xlabel('Time (ms)', fontsize=22)
plt.title('K', loc='left', y=1.05, x=-0.06, fontsize=22)
plt.tick_params(axis='x', labelsize=22)
plt.tick_params(axis='y', labelsize=22)
plt.subplots_adjust(bottom=0.5, right=0.8, top=1)

plt.legend(bbox_to_anchor=(0.23, 0.40, 0.5, 0.02), loc='best', fontsize=20,
           ncol=2, mode="expand", borderaxespad=0.)

plt.tight_layout(pad=0.5, w_pad=4, h_pad=4)
plt.savefig("Figure2.png")


