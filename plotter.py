#!/bin/python3

import matplotlib as mplt
import matplotlib.pyplot as plt

# DOC
# non-interactive backends: agg, cairo, pdf, pgf, ps, svg, template
# interactive backends: GTK3{Agg,Cairo}, MacOSX, nbAgg, Qt{4,5}{Agg,Cairo}, Tk{Agg,Cairo},
#                       WebAgg, WX{_,Agg,Cairo}
mplt.use("TkAgg")

def plot_perf_graphs():
    # files that will be read
    userMarks = open("user_fac_marks.txt", "r")
    mathlibMarks = open("mathlib_fac_marks.txt", "r")

    # plot config
    plt.xlim(0,1000)
    plt.ylim(0,1000)

# FIXME!
x = [i for i in range(1, 100)]
y = [2 * i for i in x]

u = x
v = [j ** 2 for j in u]

# axis lenght (arguments are a range)
plt.xlim(1,100)
plt.ylim(1,1000)

# axis labels
plt.xlabel("n", loc = "center")
plt.ylabel("time", loc = "center")

# plotting
# plot arguments are (x, y, color="<color>", linestyle="<style>", marker="<str>",
# makerfacecolor="<color>", markersize=<int>)
plt.plot(x, y)

plt.plot(u, v)

plt.legend(["x*2", "x**2"])

plt.title("time comparison")

# plt.savefig(fname, dpi=, facecolor=, edgecolor=, orientation=, papertype=, format=,
# transparent=, bbox_inches=, pad_inches=, frameon=, metadata=)
plt.savefig("time_plot.png", dpi=300, format="png")

plt.show()
