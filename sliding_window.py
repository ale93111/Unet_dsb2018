# -*- coding: utf-8 -*-
"""
Created on Tue May  1 17:13:37 2018

@author: alessandro
"""

#https://github.com/adamrehn/slidingwindow/blob/master/slidingwindow/SlidingWindow.py

import math

def getIndexForPatches(width, height, maxWindowSize, overlapPercent):
    """
    Generates a set of sliding windows for a dataset with the specified dimensions and order.
    """
    	
    # If the input data is smaller than the specified window size,
    # clip the window size to the input size on both dimensions
    windowSizeX = min(maxWindowSize, width)
    windowSizeY = min(maxWindowSize, height)
    
    # Compute the window overlap and step size
    windowOverlapX = int(math.floor(windowSizeX * overlapPercent))
    windowOverlapY = int(math.floor(windowSizeY * overlapPercent))
    stepSizeX = windowSizeX - windowOverlapX
    stepSizeY = windowSizeY - windowOverlapY
    
    # Determine how many windows we will need in order to cover the input data
    lastX = width - windowSizeX
    lastY = height - windowSizeY
    xOffsets = list(range(0, lastX+1, stepSizeX))
    yOffsets = list(range(0, lastY+1, stepSizeY))
    	
    # Unless the input data dimensions are exact multiples of the step size,
    # we will need one additional row and column of windows to get 100% coverage
    if len(xOffsets) == 0 or xOffsets[-1] != lastX:
        xOffsets.append(lastX)
    if len(yOffsets) == 0 or yOffsets[-1] != lastY:
        yOffsets.append(lastY)
         
    # Generate the list of windows
    windows = []
    for xOffset in xOffsets:
        for yOffset in yOffsets:
            windows.append((slice(yOffset, yOffset+windowSizeY),
                            slice(xOffset, xOffset+windowSizeX)))

	
    return windows