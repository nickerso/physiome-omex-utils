# To reproduce Figure 5 in the associated Physiome paper,
# execute this script from the command line:
#
#   cd [PathToThisFile]
#   [PathToOpenCOR]/pythonshell Figure5.py

import opencor as opencor

import numpy as np
import matplotlib

matplotlib.use('agg')
import matplotlib.pyplot as plt

# different values for y_shift
y_shift = [-15, -10, -5, 0, 5, 10, 15]
t = ["time"]
V_m = {}

# load the reference model
simulation = opencor.open_simulation("HumanSAN_Fabbri_Fantini_Wilders_Severi_2017.sedml")
data = simulation.data()
data.set_ending_point(1.9)
data.set_point_interval(0.001)

V_ode_list = []
i_tot_list = []
for y in y_shift:
    # reset everything in case we are running interactively and have existing results
    simulation.reset(True)
    simulation.clear_results()
    data.constants()["i_f/i_f_y_gate/y_shift"] = y
    for _ in range(10):
        simulation.run()
        simulation.clear_results()
    simulation.run()
    ds = simulation.results().data_store()
    V_m[str(y)] = ds.voi_and_variables()["Membrane/V"].values()
    V_ode_list.append(V_m[str(y)])
    V_m["i_tot_{}".format(str(y))] = ds.voi_and_variables()["Membrane/i_tot"].values()
    i_tot_list.append(V_m["i_tot_{}".format(str(y))])

simulation.reset(True)

Time = {}

simulation.run()
ds = simulation.results().data_store()
Time[t[0]] = ds.voi_and_variables()["environment/time"].values()

V_m.update(Time)

simulation.reset(True)


def _initialize_figure(size: tuple):
    plt.figure(figsize=size)


def _curation_plot(sub, x_variable, y_variable, c, m, ms, ls, lb, lw,
                   yl, xl, yt, xt, xlable, ylable, title, grid=False):
    """

    :param sub: number of subplots.
    :param x_variable: values of x axis.
    :param y_variable: values of y axis.
    :param c: colour.
    :param m: marker type.
    :param ms: marker size.
    :param ls: line style.
    :param lb: label.
    :param lw: line width.
    :param grid: True or False
    :return:
    """
    plt.subplot(sub[0], sub[1], sub[2])
    plt.plot(x_variable, y_variable, c, linestyle=ls, marker=m, markersize=ms, label=lb, linewidth=lw)
    if grid:
        plt.grid()
    plt.ylim(yl[0], yl[1])
    plt.yticks(np.arange(yt[0], yt[1], yt[2]))
    plt.xlabel(xlable, fontsize=26)
    plt.tick_params(axis='both', labelsize=22)
    plt.ylabel(ylable, fontsize=24)
    plt.title(title, loc='left', y=1.05, x=-0.06, fontsize='22')
    plt.tight_layout(pad= 3.0)


def plot_cl(x, y):
    _curation_plot((2, 2, 1), x, y, 'navy', 'D', '14', '', '', 3, (400, 1200), None, (400, 1300, 200), None,
                   'y$_{\infty}$ shift', 'CL (ms)', 'A', False)


def plot_ddr(x, y):
    _curation_plot((2, 2, 2), x, y, 'navy', 'D', '14', '', '', 3, (20, 80), None, (20, 90, 20), None,
                   'y$_{\infty}$ shift', 'DDR$_{100}$ (mV/s)', 'B', False)


def plot_mdp(x, y):
    _curation_plot((2, 2, 3), x, y, 'navy', 'D', '14', '', '', 3, (-65, -50), None, (-65, -45, 5), None,
                   'y$_{\infty}$ shift', 'MDP (mV)', 'C', False)


def plot_apd90(x, y):
    _curation_plot((2, 2, 4), x, y, 'navy', 'D', '14', '', '', 3, (150, 180), None, (150, 190, 10), None,
                   'y$_{\infty}$ shift', 'APD$_{90}$ (ms)', 'D', False)


def compute_apd90(i_tot, V_ode):
    top = []
    for i in range(1, len(i_tot)):
        if (-i_tot[i] >= 0.5) and (-i_tot[i - 1] <= 0.5):
            top.append(i)
    # min
    mdp = []
    for i in range(1, len(V_ode) - 1):
        if (V_ode[i] < V_ode[i - 1]) and (V_ode[i] < V_ode[i + 1]):
            mdp.append(i)

    # max
    ap = []
    for i in range(1, len(V_ode) - 1):
        if (V_ode[i] > V_ode[i - 1]) and (V_ode[i] > V_ode[i + 1]):
            ap.append(i)

    apd = []
    for i in range(1, len(top)):
        if i < len(mdp) and mdp[i] > top[i]:

            j = V_ode[top[i - 1]:mdp[i - 1]][
                V_ode[top[i - 1]:mdp[i - 1]] >= V_ode[mdp[i - 1]] + (1 - 90 / 100) * (
                            max(V_ode[top[i - 1]:mdp[i - 1]]) - V_ode[mdp[i - 1]])]
            j = list(np.where(V_ode == j[-1]))[-1]
            t = j - top[i - 1]
            apd.append(t)
        elif i + 1 <= len(mdp) and mdp[i] < top[i]:
            j = V_ode[top[i - 1]:mdp[i]][
                V_ode[top[i - 1]:mdp[i]] >= V_ode[mdp[i]] + (1 - 90 / 100) * (
                            max(V_ode[top[i - 1]:mdp[i]]) - V_ode[mdp[i]])]
            j = list(np.where(V_ode == j[-1]))[-1]
            t = j - top[i - 1]
            apd.append(t)

    return apd


if __name__ == '__main__':
    y_shift = [-15, -10, -5, 0, 5, 10, 15]

    _initialize_figure((17, 16))

    """ Plotting CL """
    cl_final = []
    for col in range(len(y_shift)):
        mdp = []
        V_ode = V_ode_list[col]
        for i in range(1, len(V_ode) - 1):
            if (V_ode[i] < V_ode[i - 1]) and (V_ode[i] < V_ode[i + 1]):
                mdp.append(i)
        cl = []
        for j in range(0, len(mdp) - 1):
            a = mdp[j + 1] - mdp[j]
            cl.append(a)
        cl_final.append(sum(cl) / len(cl))

    plot_cl(y_shift, cl_final)

    """ Plotting DDR """
    DDR = []
    for col in range(len(y_shift)):
        A = V_ode_list[col][10:800].min()
        end = (((np.where(V_ode_list[col] == V_ode_list[col][10:800].min()))[0]) + 100)
        B = V_ode_list[col][end]
        DDR.append((B - A) * 10)
    plot_ddr(y_shift, DDR)

    """ Plotting MDP """
    mdp_final = []
    for col in range(len(V_ode_list)):
        mdp = []
        V_ode = V_ode_list[col]
        for i in range(1, len(V_ode) - 1):
            if (V_ode[i] < V_ode[i - 1]) and (V_ode[i] < V_ode[i + 1]):
                mdp.append(i)
        mdp_final.append(sum(V_ode[mdp] / len(mdp)))

    plot_mdp(y_shift, mdp_final)

    """ Plotting ADP90 """
    apd90 = []
    for i in range(0, 7):
        i_tot = i_tot_list[i] * 1000 / 57
        v_ode = V_ode_list[i]
        result = compute_apd90(i_tot, v_ode)
        mean = sum(result) / len(result)
        apd90.append(mean)
    plot_apd90(y_shift, apd90)

    plt.savefig('Figure5.png')

