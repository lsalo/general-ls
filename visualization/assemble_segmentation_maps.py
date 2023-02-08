#!/usr/bin/env python3
import subprocess
import numpy as np
import generate_segmented_images as seg

fileNames = ["../../austin/spatial_maps/spatial_map_24h.csv",
             "../../csiro/spatial_map_24h.csv",
             "../../delft/delft-DARSim/spatial_map_24h.csv",
             "../../delft/delft-DARTS/spatial_map_24h.csv",
             "../../heriot-watt/spatial_map_24h.csv",
             "../../lanl/spatial_map_24h.csv",
             "../../melbourne/spatial_map_24h.csv",
             "../../stanford/spatial_maps/spatial_map_24h.csv",
             "../../stuttgart/spatial_map_24h.csv",
             "../../mit/results/m1/spatial_map_24h.csv",
             "../../mit/results/m2/spatial_map_24h.csv",
             "../../mit/results/m3_D1/spatial_map_24h.csv",
             "../../mit/results/m3_D3/spatial_map_24h.csv"]
groups = ["austin", "csiro", "darsim", "darts", "heriot_watt", "lanl", 
          "melbourne", "stanford", "stuttgart", "m1", "m2", "m3,1", "m3,3"]
nBaseGroups = 9
numGroups = len(groups)

experimentalData = np.loadtxt("../../experiment/benchmarkdata/spatial_maps/run2/segmentation_24h.csv", dtype="int", delimiter=",")
# skip the first 30 rows as they are not contained in the modeling results
experimentalData = experimentalData[30:, :]

for fileName, group in zip(fileNames, groups):
    print(f"Processing {fileName}.")
    if group != "heriot_watt":
        modelResult = seg.generateSegmentMap(fileName, 0.0, 2.86, 0.0, 1.23, 1e-2, 1e-1)
    else:
        modelResult = seg.generateSegmentMap(fileName, 0.03, 2.83, 0.03, 1.23, 1e-2, 1e-1)
    if group == "m1" or group == "m2" or group == "m3,1" or group == "m3,3":
        seg.generateImages(modelResult, experimentalData, f"z{group}_run2_24h", onlyModCont=True)
    else:
        seg.generateImages(modelResult, experimentalData, f"{group}_run2_24h", onlyModCont=True)

subprocess.run(["montage", "-tile", "3x5", "-geometry", "560x240+5+5", "*_run2_24h_mod_cont.png", "temp.png"])
subprocess.run(["convert", "temp.png", "-font", "helvetica-bold", "-fill", "yellow", "-pointsize", "48",
                "-stroke", "black",
                "-annotate", "+10+45", "Austin", "-annotate", "+580+45", "CSIRO", "-annotate",
                "+1150+45", "Delft-DARSim", "-annotate", "+10+295", "Delft-DARTS", "-annotate", "+580+295",
                "Heriot-Watt", "-annotate", "+1150+295", "LANL", "-annotate", "+10+545", "Melbourne",
                "-annotate", "+580+545", "Stanford", "-annotate", "+1150+545", "Stuttgart", 
                "-annotate", "+10+795", "m1", "-annotate", "+580+795", "m2",
                "-annotate", "+1150+795", "m3,1", "-annotate", "+10+1045", "m3,3",
                f"compare_segmentation_24h_mit.png"])
subprocess.run(["rm", "austin_run2_24h_mod_cont.png", "csiro_run2_24h_mod_cont.png", "darsim_run2_24h_mod_cont.png",
                "darts_run2_24h_mod_cont.png", "heriot_watt_run2_24h_mod_cont.png", "lanl_run2_24h_mod_cont.png",
                "melbourne_run2_24h_mod_cont.png", "stanford_run2_24h_mod_cont.png", "stuttgart_run2_24h_mod_cont.png",
                "zm1_run2_24h_mod_cont.png", "zm2_run2_24h_mod_cont.png", "zm3,1_run2_24h_mod_cont.png", 
                "zm3,3_run2_24h_mod_cont.png", "temp.png"])
print("Generated compare_segmentation_24h_mit.png.")
