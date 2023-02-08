#!/usr/bin/env python3
import os
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib

def visualizeRow(means, stddevs, expData, ax, colors):
    median = np.nanpercentile(means, 50)
    dev = np.nanpercentile(stddevs, 50)

    ax.plot([1.0, 2.0], [median, median], linewidth=2, color='xkcd:brown')
    ax.plot([1.5, 1.5], [median - dev, median + dev], linewidth=1, linestyle='dashed', color='xkcd:brown')
    ax.plot([1.4, 1.6], [median - dev, median - dev], linewidth=1, color='xkcd:brown')
    ax.plot([1.4, 1.6], [median + dev, median + dev], linewidth=1, color='xkcd:brown')
    ax.scatter(1.2*np.ones(len(means)), means, s=96, c=colors)

    mean = expData[6]
    dev = expData[7]

    ax.plot([2.5, 3.5], [mean, mean], linewidth=2, color='k')
    ax.plot([3.0, 3.0], [mean - dev, mean + dev], linewidth=1, linestyle='dashed', color='k')
    ax.plot([2.9, 3.1], [mean - dev, mean - dev], linewidth=1, color='k')
    ax.plot([2.9, 3.1], [mean + dev, mean + dev], linewidth=1, color='k')
    ax.scatter(2.7*np.ones(5), expData[1:6], s=96, c='k')

def compareSparseData():
    """Compare sparse data for the FluidFlower benchmark"""

    parser = argparse.ArgumentParser(
        description="This script compares the sparse data "
                    "as required by the benchmark description."
    )

    fileNames = ["../../austin/sparse_data.csv",
                 "../../csiro/sparse_data.csv",
                 "../../delft/delft-DARSim/sparse_data.csv",
                 "../../delft/delft-DARTS/sparse_data.csv",
                 "../../heriot-watt/HWU-sparsedata-final.csv",
                 "../../lanl/sparse_data.csv",
                 "../../melbourne/sparse_data.csv",
                 "../../stanford/sparse_data.csv",
                 "../../stuttgart/sparse_data.csv"]
    groups = ["Austin", "CSIRO", "Delft-DARSim", "Delft-DARTS", "Heriot-Watt", "LANL", "Melbourne", "Stanford", "Stuttgart"]
    colors = ["C0", "C1", "C2", "C3", "C4", "C6", "C7", "C8", "C9"]

    font = {'family' : 'normal',
            'weight' : 'normal',
            'size' : 18}
    matplotlib.rc('font', **font)
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "monospace",
    })

    numGroups = len(groups)
    numMeasurables = 13
    means = np.zeros((numMeasurables, numGroups))
    stddevs = np.zeros((numMeasurables, numGroups))
    for i, fileName in zip(range(numGroups), fileNames):
        print(f'Processing {fileName}.')

        skip_header = 0
        with open(fileName, "r") as file:
            if not (file.readline()[0]).isnumeric():
                skip_header = 1

        delimiter = ','
        skip_footer = 0

        csvData = np.genfromtxt(fileName, delimiter=delimiter, skip_header=skip_header, skip_footer=skip_footer)

        means[:, i] = csvData[:, 2]
        stddevs[:, i] = csvData[:, 5]

    expName = '../../experiment/benchmarkdata/sparse_data/sparse_data.csv'
    expData = np.genfromtxt(expName, delimiter=',', skip_header=1, skip_footer=0)

    figP, axsP = plt.subplots(1, 2, figsize=(10, 5))
    visualizeRow(means[0, :]/1e5, stddevs[0, :]/1e5, expData[0, :]/1e5, axsP[0], colors)
    axsP[0].set_ylabel(r'\textrm{\LARGE pressure [bar]}')
    axsP[0].set_title(r'\textrm{\textbf{\Large 1a: expected maximum pressure at sensor 1}}')
    axsP[0].set_xticks([1.5, 3.0])
    axsP[0].set_xticklabels([r'\textrm{\LARGE modeling}', r'\textrm{\LARGE experiment}'])
    visualizeRow(means[1, :]/1e5, stddevs[1, :]/1e5, expData[1, :]/1e5, axsP[1], colors)
    axsP[1].set_title(r'\textrm{\textbf{\Large 1b: expected maximum pressure at sensor 2}}')
    axsP[1].set_xticks([1.5, 3.0])
    axsP[1].set_xticklabels([r'\textrm{\LARGE modeling}', r'\textrm{\LARGE experiment}'])
    axsP[1].set_yticks([1.04, 1.05, 1.06, 1.07, 1.08])
    figP.tight_layout()
    figP.savefig('compare_sparse_pressure.pdf', bbox_inches='tight')

    figT, axsT = plt.subplots(1, 2, figsize=(10, 5))
    visualizeRow(means[2, :]/60/60, stddevs[2, :]/60/60, expData[2, :]/60/60, axsT[0], colors)
    axsT[0].set_ylabel(r'\textrm{\LARGE time [h]}')
    axsT[0].set_title(r'\textrm{\textbf{\Large 2: maximum mobile gaseous CO$_2$ in Box A}}')
    axsT[0].set_ylim((3.7, 5.3))
    axsT[0].set_xticks([1.5, 3.0])
    axsT[0].set_xticklabels([r'\textrm{\LARGE modeling}', r'\textrm{\LARGE experiment}'])
    visualizeRow(means[11, :]/60/60, stddevs[11, :]/60/60, expData[11, :]/60/60, axsT[1], colors)
    visualizeRow(means[11, :]/60/60, stddevs[11, :]/60/60, expData[12, :]/60/60, axsT[1], colors)
    axsT[1].set_title(r'\textrm{\textbf{\Large 5: $M(t)$ exceeds 110\% of Box C’s width}}')
    axsT[1].set_ylim((2.5, 5.0))
    axsT[1].set_xticks([1.5, 3.0])
    axsT[1].set_xticklabels([r'\textrm{\LARGE modeling}', r'\textrm{\LARGE experiment}'])
    figT.tight_layout()
    figT.savefig('compare_sparse_time.pdf', bbox_inches='tight')

    figM, axsM = plt.subplots(1, 4, figsize=(12, 4))
    visualizeRow(1e3*means[3, :], 1e3*stddevs[3, :], 1e3*expData[3, :], axsM[0], colors)
    axsM[0].set_ylabel(r'\textrm{\LARGE mass [g]}')
    axsM[0].set_title(r'\textrm{\textbf{\Large 3a: mobile gaseous CO$_2$}}')
    axsM[0].set_xticks([1.5, 3.0])
    axsM[0].set_yticks([0.0, 0.5, 1.0, 1.5, 2.0])
    axsM[0].set_xticklabels([r'\textrm{\LARGE modeling}', r'\textrm{\LARGE experiment}'])
    visualizeRow(1e3*means[5, :], 1e3*stddevs[5, :], 1e3*expData[5, :], axsM[1], colors)
    axsM[1].set_title(r'\textrm{\textbf{\Large 3c: dissolved CO$_2$}}')
    # axsM[1].set_ylim((-0.01, 4.0))
    axsM[1].set_xticks([1.5, 3.0])
    axsM[1].set_yticks([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    axsM[1].set_xticklabels([r'\textrm{\LARGE modeling}', r'\textrm{\LARGE experiment}'])
    visualizeRow(1e3*means[7, :], 1e3*stddevs[7, :], 1e3*expData[7, :], axsM[2], colors)
    axsM[2].set_title(r'\textrm{\textbf{\Large 4a: mobile gaseous CO$_2$}}')
    axsM[2].set_ylim((-0.0001, 0.0028))
    axsM[2].set_xticks([1.5, 3.0])
    axsM[2].set_yticks([0.0, 0.001, 0.002])
    axsM[2].set_xticklabels([r'\textrm{\LARGE modeling}', r'\textrm{\LARGE experiment}'])
    visualizeRow(1e3*means[9, :], 1e3*stddevs[9, :], 1e3*expData[9, :], axsM[3], colors)
    axsM[3].set_title(r'\textrm{\textbf{\Large 4c: dissolved CO$_2$}}')
    axsM[3].set_xticks([1.5, 3.0])
    axsM[3].set_yticks([0.0, 0.5, 1.0, 1.5, 2.0])
    axsM[3].set_xticklabels([r'\textrm{\LARGE modeling}', r'\textrm{\LARGE experiment}'])
    figM.tight_layout()
    figM.savefig('compare_sparse_mass.pdf', bbox_inches='tight')

    figS, axsS = plt.subplots(1, 1, figsize=(5, 5))
    visualizeRow(1e3*means[12, :], 1e3*stddevs[12, :], 1e3*expData[13, :], axsS, colors)
    axsS.set_ylabel(r'\textrm{\LARGE mass [g]}')
    axsS.set_title(r'\textrm{\textbf{\Large 6: CO$_2$ in seal facies in Box A at 120\,h}}')
    axsS.set_ylim((0.0, 0.7))
    axsS.set_xticks([1.5, 3.0])
    axsS.set_xticklabels([r'\textrm{\LARGE modeling}', r'\textrm{\LARGE experiment}'])
    figS.tight_layout()
    figS.savefig('compare_sparse_seal.pdf', bbox_inches='tight')

if __name__ == "__main__":
    compareSparseData()
