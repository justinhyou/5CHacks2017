import os
import numpy as np
import csv
import matplotlib.path as mplPath
from datetime import datetime

frary_2d = np.array([[1, 1], [2, 5], [6, 6], [5, 0]])

#function returns how many people are at frary
def fraryCount():
    with open("11_10_2017_5_35.csv", "r") as f:
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

""" NOW implementation """

#function inquires the current time and gets closest 5 minute increment
def timeEstimate():
    currenttime = datetime.now()
    minute = currenttime.minute
    if (minute % 5 != 0):
        subtraction = minute % 5
        minute-=subtraction
    return currenttime.month, currenttime.day, currenttime.year, currenttime.hour, minute

#return the file that should be looked up for that time
def fileLookup():
    month, day, year, hour, minute = timeEstimate()
    return str(month) + "_" + str(day) + "_" + str(year) + "_" + str(hour) + "_" + str(minute) + ".csv"

""" ANYTIME implementation """

def roundtime(month, day, year, hour, minute):
    roundMinute = minute
    if (minute % 5 != 0):
        subtraction = minute % 5
        roundMinute-=subtraction
    return month, day, year, hour, roundMinute

def file(month, day, year, hour, minute):
    month, day, year, hour, minute = timeEstimate(month, day, year, hour, minute)
    return str(month) + "_" + str(day) + "_" + str(year) + "_" + str(hour) + "_" + str(minute) + ".csv"

#returns how many people are in frary at a certain time
def fraryTimeCount(month, day, year, hour, minute):
    document_name = file(month, day, year, hour, minute)
    with open(document_name, "r") as f:
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

""" Growing implementation """

def 

#main function that takes in commandline argument
def main():
	return 5

#playzone
print fileLookup()
