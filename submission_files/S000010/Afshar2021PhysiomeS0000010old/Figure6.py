# To reproduce Figure 6 in the associated Physiome paper,
# execute this script from the command line:
#
#   cd [PathToThisFile]
#   [PathToOpenCOR]/pythonshell Figure6.py

import matplotlib

# matplotlib.use('agg')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

import opencor as opencor


#different values for gf to decrease the If
K_NaCa = [1.6715, 0.3343]

# load the reference model
simulation = opencor.open_simulation("HumanSAN_Fabbri_Fantini_Wilders_Severi_2017.sedml")
data = simulation.data()
data.set_ending_point(1.8)
data.set_point_interval(0.001)

simulation.reset(True)

results = np.zeros((13, 1801))

for value in range(len(K_NaCa)):
    simulation.reset(True)
    simulation.clear_results()

    data.constants()["i_NaCa/K_NaCa"] = K_NaCa[value]

    for i in range (16):
        simulation.run()
        simulation.clear_results()

    simulation.run()

    ds = simulation.results().data_store()

    results[value] = ds.voi_and_variables()["Membrane/V"].values()

simulation.reset(True)
simulation.clear_results()
data.constants()["i_NaCa/K_NaCa"] = 0.83575

for i in range(25):
    simulation.run()
    simulation.clear_results()

simulation.run()

ds = simulation.results().data_store()

results[3] = ds.voi_and_variables()["Membrane/V"].values()

simulation.reset(True)
simulation.clear_results()
data.constants()["i_NaCa/K_NaCa"] = 3.343

for i in range(23):
    simulation.run()
    simulation.clear_results()

simulation.run()

ds = simulation.results().data_store()

results[2] = ds.voi_and_variables()["Membrane/V"].values()


for i in range(0,1):
    for i in range (3):
        simulation.run()
        simulation.clear_results()
    simulation.run()

    ds = simulation.results().data_store()
    results[4] = ds.voi_and_variables()["environment/time"].values()

for value in range(len(K_NaCa)):
    simulation.reset(True)
    simulation.clear_results()

    data.constants()["i_NaCa/K_NaCa"] = K_NaCa[value]
    for i in range (8):
        simulation.run()
        simulation.clear_results()
    simulation.run()

    ds = simulation.results().data_store()

    results[value+5] = ds.voi_and_variables()["Ca_dynamics/Cai"].values()

simulation.reset(True)
simulation.clear_results()
data.constants()["i_NaCa/K_NaCa"] = 0.83575

for i in range(11):
    simulation.run()
    simulation.clear_results()

simulation.run()

ds = simulation.results().data_store()

results[8] = ds.voi_and_variables()["Ca_dynamics/Cai"].values()

simulation.reset(True)
simulation.clear_results()
data.constants()["i_NaCa/K_NaCa"] = 3.343

for i in range(42):
    simulation.run()
    simulation.clear_results()

simulation.run()

ds = simulation.results().data_store()

results[7] = ds.voi_and_variables()["Ca_dynamics/Cai"].values()

for value in range(len(K_NaCa)):
    simulation.reset(True)
    simulation.clear_results()

    data.constants()["i_NaCa/K_NaCa"] = K_NaCa[value]
    for i in range(12):
        simulation.run()
        simulation.clear_results()
    simulation.run()

    ds = simulation.results().data_store()

    results[value+9] = ds.voi_and_variables()["i_NaCa/i_NaCa"].values()

simulation.reset(True)
simulation.clear_results()
data.constants()["i_NaCa/K_NaCa"] = 0.83575

for i in range(34):
    simulation.run()
    simulation.clear_results()

simulation.run()

ds = simulation.results().data_store()

results[12] = ds.voi_and_variables()["i_NaCa/i_NaCa"].values()

simulation.reset(True)
simulation.clear_results()
data.constants()["i_NaCa/K_NaCa"] = 3.343

for i in range(56):
    simulation.run()
    simulation.clear_results()

simulation.run()

ds = simulation.results().data_store()

results[11] = ds.voi_and_variables()["i_NaCa/i_NaCa"].values()



# define the x and y axis and match the units
X = results[4]*1000
Y1 = results[2]
Y2 =results[0]
Y3 = results[3]
Y4 = results[1]
Y5 = results[7]*1e6
Y6 = results[5]*1e6
Y7 = results[8]*1e6
Y8 = results[6]*1e6
Y9 = results[11]*1000/57
Y10 = results[9]*1000/57
Y11 = results[12]*1000/57
Y12 = results[10]*1000/57


plt.figure(figsize=(16,14))
plt.subplot(2,2,1)

plt.plot(X, Y1, 'navy',linestyle='-',  label = 'CTRL', linewidth= 3)
plt.plot(X, Y2, 'red',linestyle='-',  label = 'Block 50%', linewidth= 3)
plt.plot(X, Y3, 'green',linestyle='-',  label = 'Block 75%', linewidth= 3)
plt.plot(X, Y4, 'purple',linestyle='-',  label = 'Block 90%', linewidth= 3)


plt.gca().add_patch(Rectangle((480,-65),670,30,linewidth=2,edgecolor='black', linestyle= '--',facecolor='none'))

plt.xlim(0, 1800)
plt.ylim(-70,30)
plt.xticks(np.arange(0,1800, 500))

plt.tick_params(axis='both', labelsize=20)
plt.ylabel ('V$_m$ (mV)', fontsize=20)
plt.title('A',loc= 'left', y = 1.05, x= -0.06, fontsize='22')

plt.subplot(2,2,2)
plt.plot(X, Y1, 'navy',linestyle='-',  label = 'CTRL', linewidth= 3)
plt.plot(X, Y2, 'red',linestyle='-',  label = 'Block 50%', linewidth= 3)
plt.plot(X, Y3, 'green',linestyle='-',  label = 'Block 75%', linewidth= 3)
plt.plot(X, Y4, 'purple',linestyle='-',  label = 'Block 90%', linewidth= 3)



plt.xlim(465, 1140)
plt.ylim(-63,-35)

plt.tick_params(axis='both', labelsize=20)
plt.ylabel ('V$_m$ (mV)', fontsize=20)
plt.title('B', loc= 'left', y = 1.05, x= -0.06, fontsize='22')


plt.subplot(2,2,3)
plt.plot(X, Y5, 'navy',linestyle='-',  label = 'CTRL', linewidth= 3)
plt.plot(X, Y6, 'red',linestyle='-',  label = 'Block 50%', linewidth= 3)
plt.plot(X, Y7, 'green',linestyle='-',  label = 'Block 75%', linewidth= 3)
plt.plot(X, Y8, 'purple',linestyle='-',  label = 'Block 90%', linewidth= 3)


plt.xlim(0, 1780)
plt.xticks(np.arange(0,1800, 500))
plt.ylim(50,450)
plt.xlabel ('Time (ms)',fontsize=20)
plt.tick_params(axis='both', labelsize=20)
plt.ylabel ('[Ca$^{2+}]_i$ (nM)', fontsize=20)
plt.title('C', loc= 'left', y = 1.05, x= -0.06, fontsize='22')

plt.subplot(2,2,4)
plt.plot(X, Y9, 'navy',linestyle='-',  label = 'CTRL', linewidth= 3)
plt.plot(X, Y10, 'red',linestyle='-',  label = 'Block 50%', linewidth= 3)
plt.plot(X, Y11, 'green',linestyle='-',  label = 'Block 75%', linewidth= 3)
plt.plot(X, Y12, 'purple',linestyle='-',  label = 'Block 90%', linewidth= 3)


x = np.array([460, 500, 600, 700, 800, 900, 1000, 1090])
values = [" ", "500", "600", "700", "800", "900", "1000", "1100"]
plt.xlim(460, 1120)
plt.xticks(x, values)


plt.ylim(-0.16, 0.05)
plt.yticks(np.arange(-0.15,0.01, 0.05))
plt.xlabel ('Time (ms)',fontsize=20)
plt.tick_params(axis='both', labelsize=20)
plt.ylabel ('I$_{NaCa}$ (pA/pF)', fontsize=20)
plt.title('D', loc= 'left', y = 1.05, x= -0.06, fontsize='22')
plt.legend(bbox_to_anchor=(0.3, 0.85, 0.4, 0.1), loc='best',fontsize=20,
       ncol=1, mode="expand")


plt.tight_layout(pad= 2.5, w_pad=3.5, h_pad=3)

plt.savefig('Figure6.png')
plt.show()
