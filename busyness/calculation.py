import os
import numpy as np
import csv
import matplotlib.path as mplPath
from datetime import datetime

frary_2d = np.array([[1, 1], [2, 5], [6, 6], [5, 0]])

#function returns how many people are at frary
def fraryCount():
    with open("tues_11_10_2017_5_35.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        counter = 0
        boundary = mplPath.Path(frary_2d)
        header = True
        for line in reader:
            if (header):
                header = False
                continue
            if (boundary.contains_point((int(line[0]), int(line[1])))):
                counter+=1
    return counter

#function inquires the current time and gets closest 5 minute increment
def timeEstimate():
    return datetime.now()
#    return 'tues_11_10_2017_5_35.csv'


#main function that takes in commandline argument
def main():
	return 5

#playzone
print timeEstimate()
