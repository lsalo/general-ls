"""
Generate images with script generate_grayscale.py
"""
import numpy as np
import os.path
import emd

baseFileNames = ['../../austin/figures/austin_lasergrid_',
                  '../../csiro/figures/csiro_lasergrid_',
                  '../../delft/delft-DARSim/figures/darsim_lasergrid_',
                  '../../delft/delft-DARTS/figures/darts_lasergrid_',
                  '../../heriot-watt/figures/heriot_watt_lasergrid_',
                  '../../lanl/figures/lanl_lasergrid_',
                  '../../melbourne/Figures/melbourne_lasergrid_',
                  '../../stanford/figures/stanford_lasergrid_',
                  '../../stuttgart/figures/stuttgart_lasergrid_',
                  '../../mit/results/revised/m1/mit_lasergrid_',
                  '../../mit/results/revised/m2/mit_lasergrid_',
                  '../../mit/results/revised/m3_D1/mit_lasergrid_',
                  '../../mit/results/revised/m3_D3/mit_lasergrid_']
# baseFileNames = ['../../austin/spatial_maps/spatial_map_grayscale_',
#                  '../../csiro/spatial_map_grayscale_',
#                  '../../delft/delft-DARSim/spatial_map_grayscale_',
#                  '../../delft/delft-DARTS/spatial_map_grayscale_',
#                  '../../heriot-watt/figures/heriot_watt_gray_',
#                  '../../lanl/figures/lanl_gray_',
#                  '../../melbourne/figures/melbourne_gray_',
#                  '../../stanford/figures/stanford_gray_',
#                  '../../stuttgart/figures/stuttgart_gray_']

numGroups = len(baseFileNames)
distances = np.zeros((numGroups*5, numGroups*5))

for hourI in [24, 48, 72, 96, 120]:
    for hourJ in [24, 48, 72, 96, 120]:
        if hourJ < hourI: continue

        for i, baseFileNameI in zip(range(numGroups), baseFileNames):
            fileNameI = baseFileNameI + str(hourI) + 'h.png'
            if (os.path.exists(fileNameI)):
                row = int((hourI/24 - 1)*numGroups + i)

                for j, baseFileNameJ in zip(range(numGroups), baseFileNames):
                    if j <= i and hourJ == hourI: continue

                    fileNameJ = baseFileNameJ + str(hourJ) + 'h.png'
                    if (os.path.exists(fileNameJ)):
                        col = int((hourJ/24 - 1)*numGroups + j)

                        distances[row][col] = emd.calculateEMD(fileNameI, fileNameJ)

                        print(f'{hourI}, {hourJ}, {i}, {j} -> ({row}, {col}): {distances[row][col]}')

distances = distances + distances.T - np.diag(distances.diagonal())

np.savetxt("distances_mit_revised.csv", distances, delimiter=",")
