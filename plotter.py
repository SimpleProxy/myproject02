#!/bin/python3

import matplotlib as mplt
import matplotlib.pyplot as plt

# DOC
# non-interactive backends: agg, cairo, pdf, pgf, ps, svg, template
# interactive backends: GTK3{Agg,Cairo}, MacOSX, nbAgg, Qt{4,5}{Agg,Cairo}, Tk{Agg,Cairo},
#                       WebAgg, WX{_,Agg,Cairo}
mplt.use("TkAgg")

def plot_user_fac_graph():
    userMarks = open("./results/vector_nxt_user.txt", "r")
    userMarks.seek(0,0)

    x = []
    y = []

    for line in userMarks.readlines():
        n,t = line.split()
        x.append(int(n))
        y.append(int(t))

    # plot config
    plt.xlim(min(x), max(x))
    plt.ylim(min(y), max(y))

    # axis labels
    plt.xlabel("N", loc = "center", fontsize=10)
    plt.ylabel("time", loc = "center", fontsize=10)

    # plotting
    # plot arguments are (x, y, color="<color>", linestyle="<style>", marker="<str>",
    # makerfacecolor="<color>", markersize=<int>)
    p1 = plt.plot(x, y, color="green",
             linewidth=1, linestyle="dotted", markersize=5,
             label="user")

    plt.legend(loc="upper left")

    # plt.savefig(fname, dpi=, facecolor=, edgecolor=, orientation=, papertype=, format=,
    # transparent=, bbox_inches=, pad_inches=, frameon=, metadata=)
    plt.savefig("./graphs/plot_user_time.png", dpi=300, format="png")

    plt.clf() # clear current figure


def plot_math_fac_graph():
    mathlibMarks = open("./results/vector_nxt_mathlib.txt", "r")
    mathlibMarks.seek(0,0)

    u = []
    v = []

    for line in mathlibMarks.readlines():
        n,t = line.split()
        u.append(int(n))
        v.append(int(t))

    # plot config
    plt.xlim(min(u), max(u))
    plt.ylim(min(v), max(v))

    # axis labels
    plt.xlabel("N", loc = "center")
    plt.ylabel("time", loc = "center")

    plt.plot(u, v, color="red",
             linewidth=1, linestyle="solid", markersize=5,
             label="mathlib")

    plt.legend(loc="upper left")

    #plt.title("time comparison")

    # plt.savefig(fname, dpi=, facecolor=, edgecolor=, orientation=, papertype=, format=,
    # transparent=, bbox_inches=, pad_inches=, frameon=, metadata=)
    plt.savefig("./graphs/plot_math_time.png", dpi=300, format="png")

    plt.clf() # clear current figure

def plot_vm_fac_graph():
    vmMarks = open("./results/vector_nxt_vm.txt", "r")
    vmMarks.seek(0,0)

    z = []
    w = []

    for line in vmMarks.readlines():
        n,t = line.split()
        z.append(int(n))
        w.append(int(t))

    # plot config
    plt.xlim(min(z), max(z))
    plt.ylim(min(w), max(w))

    # axis labels
    plt.xlabel("N", loc = "center")
    plt.ylabel("time", loc = "center")

    # plotting
    plt.plot(z, w, color="blue",
             linewidth=1, linestyle="dashed", markersize=5,
             label="VM")

    plt.legend(loc="upper left")

    plt.savefig("./graphs/plot_vm_time.png", dpi=300, format="png")

    plt.clf() # clear current figure

plot_math_fac_graph()
plot_user_fac_graph()
plot_vm_fac_graph()
