# set working directory to fluidflower/general-ls/
import sys
sys.path.append('visualization/')
sys.path.append('evaluation/')
import generate_grayscale_lasergrid as lsg
#import generate_grayscale as gsc
import os
import argparse

baseFileNames = ['mit/results/revised/m1/',
                 'mit/results/revised/m2/',
                 'mit/results/revised/m3_D1/',
                 'mit/results/revised/m3_D3/']
reportTimes = [24, 48, 72, 96, 120]

for fileName in baseFileNames:
    os.chdir('/Users/lluis/Documents/python/fluidflower/' + fileName)
    for tstep in reportTimes:
        lsg.generateGrayScale(input_name = "spatial_map_" + str(tstep) + "h.csv",
                              output_name= "mit_lasergrid_" + str(tstep) + "h.png")
        #gsc.generateGrayScale()
