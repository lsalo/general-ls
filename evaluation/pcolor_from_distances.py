import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors

font = {'family' : 'normal',
        'weight' : 'normal',
        'size' : 14}
matplotlib.rc('font', **font)
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "monospace",
})

groups = ["Austin", "CSIRO", "Delft-DARSim", "Delft-DARTS", "Heriot-Watt", 
          "LANL", "Melbourne", "Stanford", "Stuttgart", "m1", "m2", "m3_1", "m3_3"]
colors = ["C0", "C1", "C2", "C3", "C4", "C6", "C7", "C8", "C9", "C5", "C5", "C5", "C5"]

numGroups = len(groups)
nBaseGroups = 9

distances = np.loadtxt("distances_mit.csv", delimiter=",")

cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["white","red"])

fig, axs = plt.subplots(1, 2, figsize=(14, 4))

# The calculated distances have the unit of normalized mass times meter.
# Multiply by 8.5, the injected mass of CO2 in g, and 100, to convert to g.cm.
A = 850*distances[:numGroups, :numGroups]
# remove values related to LANL
A = np.delete(A, 5, 0)
A = np.delete(A, 5, 1)
#meanA = np.mean(A, axis=0) 
meanA = np.mean(A[:nBaseGroups-1, :], axis=0) #don't consider MIT bc they form a cluster
A = A + np.diag(meanA)
A = np.flip(A, 0)

groups.remove("LANL")
colors.remove("C6")
axs[0].pcolor(A, cmap=cmap)
axs[0].set_yticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5])
axs[0].set_yticklabels(reversed(groups))
for i in range(numGroups-1):
    axs[0].get_yticklabels()[i].set_color(colors[numGroups-2-i])
axs[0].set_xticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5])
axs[0].set_xticklabels(groups, rotation=45, ha="right")
for i in range(numGroups-1):
    axs[0].get_xticklabels()[i].set_color(colors[i])
for (i,j), value in np.ndenumerate(A):
    if i >= numGroups-2-j:
        if value > 0:
            axs[0].text(numGroups-1-i-0.5, numGroups-1-j-0.6, f'{int(value):03d}', ha='center', va='center')
        else:
            axs[0].text(numGroups-1-i-0.5, numGroups-1-j-0.6, '-', ha='center', va='center')
axs[0].set_title(r"\textrm{\textbf{24 hours}}")

A = 850*distances[4*numGroups:, 4*numGroups:]
# remove values related to LANL
A = np.delete(A, 5, 0)
A = np.delete(A, 5, 1)
#meanA = np.mean(A, axis=0)*8/7 # take correct avg due to missing HW data 
meanA = np.mean(A[:nBaseGroups-1, :], axis=0)*8/7
A = A + np.diag(meanA)
A = np.flip(A, 0)

axs[1].pcolor(A, cmap=cmap)
axs[1].tick_params(axis='y', which='both', left=False, right=True, labelleft=False, labelright=True)
axs[1].set_yticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5])
axs[1].set_yticklabels(reversed(groups))
for i in range(numGroups-1):
    axs[1].get_yticklabels()[i].set_color(colors[numGroups-2-i])
axs[1].set_xticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5])
axs[1].set_xticklabels(groups, rotation=45, ha="right")
for i in range(numGroups-1):
    axs[1].get_xticklabels()[i].set_color(colors[i])
for (i,j), value in np.ndenumerate(A):
    if i >= numGroups-2-j:
        if value > 0:
            axs[1].text(numGroups-1-i-0.5, numGroups-1-j-0.6, f'{int(value):03d}', ha='center', va='center')
        else:
            axs[1].text(numGroups-1-i-0.5, numGroups-1-j-0.6, '-', ha='center', va='center')
axs[1].set_title(r"\textrm{\textbf{120 hours}}")

fig.savefig(f"pcolor_distances_mit.pdf", bbox_inches='tight')
