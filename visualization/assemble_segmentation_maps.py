#!/usr/bin/env python3
import subprocess
import numpy as np
import generate_segmented_images as seg

time_h = "120"
fileNames = ["../../austin/spatial_maps/spatial_map_",
             "../../csiro/spatial_map_",
             "../../delft/delft-DARSim/spatial_map_",
             "../../delft/delft-DARTS/spatial_map_",
             "../../heriot-watt/spatial_map_",
             "../../lanl/spatial_map_",
             "../../melbourne/spatial_map_",
             "../../stanford/spatial_maps/spatial_map_",
             "../../stuttgart/spatial_map_",
             "../../mit/results/m1/spatial_map_",
             "../../mit/results/m2/spatial_map_",
             "../../mit/results/m3_D1/spatial_map_",
             "../../mit/results/m3_D3/spatial_map_"]
groups = ["austin", "csiro", "darsim", "darts", "heriot_watt", "lanl", 
          "melbourne", "stanford", "stuttgart", "m1", "m2", "m3,1", "m3,3"]
nBaseGroups = 9
numGroups = len(groups)

experimentalData = np.loadtxt(f"../../experiment/benchmarkdata/spatial_maps/run2/segmentation_{time_h}h.csv", 
                              dtype="int", delimiter=",")
# skip the first 30 rows as they are not contained in the modeling results
experimentalData = experimentalData[30:, :]

for fileName, group in zip(fileNames, groups):
    print(f"Processing {fileName}.")
    if group != "heriot_watt":
        modelResult = seg.generateSegmentMap(f"{fileName}{time_h}h.csv", 0.0, 2.86, 0.0, 1.23, 1e-2, 1e-1)
    else:
        if time_h == "24" or time_h == "48":
            modelResult = seg.generateSegmentMap(f"{fileName}{time_h}h.csv", 0.03, 2.83, 0.03, 1.23, 1e-2, 1e-1)
        else:
            modelResult = np.zeros((120, 280))
    if group == "m1" or group == "m2" or group == "m3,1" or group == "m3,3":
        seg.generateImages(modelResult, experimentalData, f"z{group}_run2_{time_h}h", onlyModCont=True)
    else:
        seg.generateImages(modelResult, experimentalData, f"{group}_run2_{time_h}h", onlyModCont=True)

subprocess.run(["montage", "-tile", "3x5", "-geometry", "560x240+5+5", f"*_run2_{time_h}h_mod_cont.png", "temp.png"])
subprocess.run(["convert", "temp.png", "-font", "helvetica-bold", "-fill", "yellow", "-pointsize", "48",
                "-stroke", "black",
                "-annotate", "+10+45", "Austin", "-annotate", "+580+45", "CSIRO", "-annotate",
                "+1150+45", "Delft-DARSim", "-annotate", "+10+295", "Delft-DARTS", "-annotate", "+580+295",
                "Heriot-Watt", "-annotate", "+1150+295", "LANL", "-annotate", "+10+545", "Melbourne",
                "-annotate", "+580+545", "Stanford", "-annotate", "+1150+545", "Stuttgart", 
                "-annotate", "+10+795", "m1", "-annotate", "+580+795", "m2",
                "-annotate", "+1150+795", "m3,1", "-annotate", "+10+1045", "m3,3",
                f"compare_segmentation_{time_h}h_mit.png"])
subprocess.run(["rm", f"austin_run2_{time_h}h_mod_cont.png", f"csiro_run2_{time_h}h_mod_cont.png", f"darsim_run2_{time_h}h_mod_cont.png",
                f"darts_run2_{time_h}h_mod_cont.png", f"heriot_watt_run2_{time_h}h_mod_cont.png", f"lanl_run2_{time_h}h_mod_cont.png",
                f"melbourne_run2_{time_h}h_mod_cont.png", f"stanford_run2_{time_h}h_mod_cont.png", f"stuttgart_run2_{time_h}h_mod_cont.png",
                f"zm1_run2_{time_h}h_mod_cont.png", f"zm2_run2_{time_h}h_mod_cont.png", f"zm3,1_run2_{time_h}h_mod_cont.png", 
                f"zm3,3_run2_{time_h}h_mod_cont.png", "temp.png"])
print(f"Generated compare_segmentation_{time_h}h_mit.png.")
