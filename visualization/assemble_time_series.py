#!/usr/bin/env python3
import os
import argparse
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def assembleTimeSeries():
    """Visualize time series for the FluidFlower benchmark"""

    parser = argparse.ArgumentParser(
        description="This script visualizes the time series quantities "
                    "as required by the benchmark description."
    )

    fileNames = ["../../austin/time_series.csv",
                 "../../csiro/time_series.csv",
                 "../../delft/delft-DARSim/time_series.csv",
                 "../../delft/delft-DARTS/time_series.csv",
                 "../../herriot-watt/HWU-FinalTimeSeries.csv",
                 "../../lanl/time_series.csv",
                 "../../melbourne/time_series.csv",
                 "../../stanford/time_series_final.csv",
                 "../../stuttgart/time_series.csv"]
    groups = ["Austin", "CSIRO", "Delft-DARSim", "Delft-DARTS", "Heriot-Watt", "LANL", "Melbourne", "Stanford", "Stuttgart"]
    colors = ["C0", "C1", "C2", "C3", "C4", "C6", "C7", "C8", "C9"]

    font = {'family' : 'normal',
            'weight' : 'normal',
            'size' : 14}
    matplotlib.rc('font', **font)
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "monospace",
    })

    figP, axsP = plt.subplots(1, 2, figsize=(12, 4))
    figPT, axsPT = plt.subplots(1, 2, figsize=(12, 4))
    figA, axsA = plt.subplots(2, 2, figsize=(12, 8))
    figB, axsB = plt.subplots(2, 2, figsize=(12, 8))
    figC, axsC = plt.subplots(figsize=(6, 4))
    figT, axsT = plt.subplots(figsize=(6, 4))

    for fileName, group, color in zip(fileNames, groups, colors):
        print(f'Processing {fileName}.')

        skip_header = 0
        with open(fileName, "r") as file:
            if not (file.readline()[0]).isnumeric():
                skip_header = 1

        delimiter = ','

        csvData = np.genfromtxt(fileName, delimiter=delimiter, skip_header=skip_header)
        t = csvData[:, 0]/60/60

        axsP[0].plot(t, csvData[:, 1]/1e5, label=group, color=color)
        axsP[0].set_title(r'\textrm{\textbf{\large sensor 1}}')
        axsP[0].set_xlabel(r'\textrm{time [h]}')
        axsP[0].set_ylabel(r'\textrm{pressure [bar]}')
        axsP[0].set_ylim(1.09e0, 1.15e0)
        axsP[0].set_xlim(-1.0/60, 7260.0/60)

        axsP[1].plot(t, csvData[:, 2]/1e5, label=group, color=color)
        axsP[1].set_title(r'\textrm{\textbf{\large sensor 2}}')
        axsP[1].set_xlabel(r'\textrm{time [h]}')
        axsP[1].set_ylim(1.03e0, 1.09e0)
        axsP[1].set_xlim(-1.0/60, 7260.0/60)

        axsPT[0].plot(t, csvData[:, 1]/1e5, label=group, color=color)
        axsPT[0].set_title(r'\textrm{\textbf{\large sensor 1}}')
        axsPT[0].set_xlabel(r'\textrm{time [h]}')
        axsPT[0].set_ylabel(r'\textrm{pressure [bar]}')
        axsPT[0].set_xlim(-0.1/60, 610.0/60)
        axsPT[0].set_ylim(1.09e0, 1.15e0)

        axsPT[1].plot(t, csvData[:, 2]/1e5, label=group, color=color)
        axsPT[1].set_title(r'\textrm{\textbf{\large sensor 2}}')
        axsPT[1].set_xlabel(r'\textrm{time [h]}')
        axsPT[1].set_xlim(-0.1/60, 610.0/60)
        axsPT[1].set_ylim(1.03e0, 1.09e0)

        axsA[0, 0].plot(t, 1e3*csvData[:, 3], label=group, color=color)
        axsA[0, 0].set_title(r'\textrm{\textbf{\large Box A: mobile gaseous CO$_2$}}')
        axsA[0, 0].set_ylabel(r'\textrm{mass [g]}')
        axsA[0, 0].set_xlim(-1.0/60, 7260.0/60)
        axsA[0, 0].set_ylim(-0.1, 3.0)

        axsA[0, 1].plot(t, 1e3*csvData[:, 4], label=group, color=color)
        axsA[0, 1].set_title(r'\textrm{\textbf{\large Box A: immobile gaseous CO$_2$}}')
        axsA[0, 1].set_xlim(-1.0/60, 7260.0/60)
        axsA[0, 1].set_ylim(-0.01, 0.3)

        axsA[1, 0].plot(t, 1e3*csvData[:, 5], label=group, color=color)
        axsA[1, 0].set_title(r'\textrm{\textbf{\large Box A: CO$_2$ dissolved in liquid phase}}')
        axsA[1, 0].set_xlabel(r'\textrm{time [h]}')
        axsA[1, 0].set_ylabel(r'\textrm{mass [g]}')
        axsA[1, 0].set_xlim(-1.0/60, 7260.0/60)
        axsA[1, 0].set_ylim(-0.01, 6.0)

        axsA[1, 1].plot(t, 1e3*csvData[:, 6], label=group, color=color)
        axsA[1, 1].set_title(r'\textrm{\textbf{\large Box A: CO$_2$ in the seal facies}}')
        axsA[1, 1].set_xlabel(r'\textrm{time [h]}')
        axsA[1, 1].set_xlim(-1.0/60, 7260.0/60)
        axsA[1, 1].set_ylim(-0.01, 1.0)

        axsB[0, 0].plot(t, 1e3*csvData[:, 7], label=group, color=color)
        axsB[0, 0].set_title(r'\textrm{\textbf{\large Box B: mobile gaseous CO$_2$}}')
        axsB[0, 0].set_ylabel(r'\textrm{mass [g]}')
        axsB[0, 0].set_xlim(-1.0/60, 7260.0/60)
        axsB[0, 0].set_ylim(-0.01, 0.6)

        axsB[0, 1].plot(t, 1e3*csvData[:, 8], label=group, color=color)
        axsB[0, 1].set_title(r'\textrm{\textbf{\large Box B: immobile gaseous CO$_2$}}')
        axsB[0, 1].set_xlim(-1.0/60, 7260.0/60)
        axsB[0, 1].set_ylim(-0.001, 0.07)

        axsB[1, 0].plot(t, 1e3*csvData[:, 9], label=group, color=color)
        axsB[1, 0].set_title(r'\textrm{\textbf{\large Box B: CO$_2$ dissolved in liquid phase}}')
        axsB[1, 0].set_xlabel(r'\textrm{time [h]}')
        axsB[1, 0].set_ylabel(r'\textrm{mass [g]}')
        axsB[1, 0].set_xlim(-1.0/60, 7260.0/60)
        axsB[1, 0].set_ylim(-0.01, 2.5)

        axsB[1, 1].plot(t, 1e3*csvData[:, 10], label=group, color=color)
        axsB[1, 1].set_title(r'\textrm{\textbf{\large Box B: CO$_2$ in the seal facies}}')
        axsB[1, 1].set_xlabel(r'\textrm{time [h]}')
        axsB[1, 1].set_xlim(-1.0/60, 7260.0/60)
        axsB[1, 1].set_ylim(-0.01, 0.6)

        axsC.plot(t, csvData[:, 11], label=group, color=color)
        axsC.set_title(r'\textrm{\textbf{\large Box C: convection}}')
        axsC.set_xlabel(r'\textrm{time [h]}')
        axsC.set_ylabel(r'\textrm{$M$ [m]}')
        axsC.set_xlim(-1.0/60, 7260.0/60)
        axsC.legend(loc='center left', bbox_to_anchor=(1, 0.5))

        axsT.plot(t, 1e3*csvData[:, 12], label=group, color=color)
        axsT.set_title(r'\textrm{\textbf{\large total CO2 mass}}')
        axsT.set_xlabel(r'\textrm{time [h]}')
        axsT.set_ylabel(r'\textrm{mass [g]}')
        axsT.set_xlim(-1.0/60, 7260.0/60)
        axsT.set_ylim(-0.01, 10.0)
        axsT.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    handles, labels = axsP[1].get_legend_handles_labels()
    figP.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=5)
    figP.savefig('time_series_pressure.pdf', bbox_inches='tight')

    handles, labels = axsPT[1].get_legend_handles_labels()
    figPT.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=5)
    figPT.savefig('time_series_pressure_zoom_time.pdf', bbox_inches='tight')

    handles, labels = axsA[1][1].get_legend_handles_labels()
    figA.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.01), ncol=5)
    figA.savefig('time_series_boxA.pdf', bbox_inches='tight')

    handles, labels = axsB[1][1].get_legend_handles_labels()
    figB.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.01), ncol=5)
    figB.savefig('time_series_boxB.pdf', bbox_inches='tight')

    figC.savefig('time_series_boxC.pdf', bbox_inches='tight')
    figT.savefig('time_series_co2mass.pdf', bbox_inches='tight')

if __name__ == "__main__":
    assembleTimeSeries()
