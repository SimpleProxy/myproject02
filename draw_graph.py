#!/bin/python3
# -*- coding: utf-8 -*-

# file name: draw_graph.py

import matplotlib as mplt
import matplotlib.pyplot as plt

# DOC
# non-interactive backends: agg, cairo, pdf, pgf, ps, svg, template
# interactive backends: GTK3{Agg,Cairo}, MacOSX, nbAgg, Qt{4,5}{Agg,Cairo}, Tk{Agg,Cairo},
#                       WebAgg, WX{_,Agg,Cairo}
mplt.use("TkAgg")
# auto adjust plots layouts
mplt.rcParams.update({"figure.autolayout": True})

def plot_graphs():
    userMarks = open("./results/vector_nxt_user.txt", "r")
    userMarks.seek(0,0)

    x = []
    y = []

    for line in userMarks.readlines():
        n,t = line.split()
        x.append(int(n))
        y.append(int(t))

    mathlibMarks = open("./results/vector_nxt_mathlib.txt", "r")
    mathlibMarks.seek(0,0)

    u = []
    v = []

    for line in mathlibMarks.readlines():
        n,t = line.split()
        u.append(int(n))
        v.append(int(t))

    vmMarks = open("./results/vector_nxt_vm.txt", "r")
    vmMarks.seek(0,0)

    z = []
    w = []

    for line in vmMarks.readlines():
        n,t = line.split()
        z.append(int(n))
        w.append(int(t))

    # plot config
    plt.xlim(min(x), max(x)) # all plots start at 1 and end at 500
    plt.ylim(min(v), max(w)) # the lesser and the greater observed time measures

    # axis labels
    plt.xlabel("N", loc = "center", fontsize=10)
    plt.ylabel("time(in nanoseconds)", loc = "center", fontsize=10)

    # plotting
    # plot arguments are (x, y, color="<color>", linestyle="<style>", marker="<str>",
    # makerfacecolor="<color>", markersize=<int>)
    plt.plot(u, v, color="red",
             linewidth=1, linestyle="solid", markersize=5,
             label="mathlib")

    plt.plot(x, y, color="green",
             linewidth=1, linestyle="dotted", markersize=5,
             label="user")

    plt.plot(z, w, color="blue",
             linewidth=1, linestyle="dashed", markersize=5,
             label="VM")

    # place the legend at the top left corner
    plt.legend(loc="upper left")

    # auto scale axis
    plt.autoscale(enable=True, axis="x", tight=True)
    plt.autoscale(enable=True, axis="y", tight=True)

    #draw a grid
    plt.grid()
    # save plots
    plt.savefig("./graphs/uni_plot.png", dpi=300, format="png")

    # close text files
    mathlibMarks.close()
    userMarks.close()
    vmMarks.close()

if __name__ == "__main__":
    plot_graphs()

