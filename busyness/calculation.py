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

#for now, the csv files live in the data folder
prepend = "/data/"
def currentfile(month, day, year, hour, minute):
    month, day, year, hour, minute = roundtime(month, day, year, hour, minute)
    #general standardization
    month = str(month)
    if len(month) < 2:
        month = "0" + month
    day = str(day)
    if len(day) < 2:
        day = "0" + day
    year = str(year)
    #hour and minute may be 00
    hour = str(hour)
    if len(hour) < 2:
        hour = "0" + hour
    minute = str(minute)
    if len(minute) < 2:
        minute = "0" + minute

    return prepend + month + "_" + day + "_" + year + "_" + hour + "_" + minute + ".csv"

#returns how many people are in frary at a certain time
def fraryTimeCount(month, day, year, hour, minute):
    document_name = currentfile(month, day, year, hour, minute)
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

""" All Dining Halls """
frary_2d = np.array([[1, 1], [2, 5], [6, 6], [5, 0]])
offset = 0.0004
frary_boundary = np.array([[34.10043-offset,-117.710929-offset],\
                            [34.10043-offset,-117.710929+offset],\
                            [34.10043+offset,-117.710929+offset],\
                            [34.10043+offset,-117.710929-offset]])
frank_boundary = np.array([[34.096107-offset,-117.711508-offset],\
                            [34.096107-offset,-117.711508+offset],\
                            [34.096107+offset,-117.711508+offset],\
                            [34.096107+offset,-117.711508-offset]])
oldenborg_boundary = np.array([[34.097131-offset,-117.711818-offset],\
                            [34.097131-offset,-117.711818+offset],\
                            [34.097131+offset,-117.711818+offset],\
                            [34.097131+offset,-117.711818-offset]])
collins_boundary = np.array([[34.101542-offset,-117.709005-offset],\
                            [34.101542-offset,-117.709005+offset],\
                            [34.101542+offset,-117.709005+offset],\
                            [34.101542+offset,-117.709005-offset]])
malott_boundary = np.array([[34.102835-offset,-117.710565-offset],\
                            [34.102835-offset,-117.710565+offset],\
                            [34.102835+offset,-117.710565+offset],\
                            [34.102835+offset,-117.710565-offset]])
hoch_boundary = np.array([[34.105763-offset,-117.709846-offset],\
                            [34.105763-offset,-117.709846+offset],\
                            [34.105763+offset,-117.709846+offset],\
                            [34.105763+offset,-117.709846-offset]])
mcconnell_boundary = np.array([[34.102840-offset,-117.705536-offset],\
                            [34.102840-offset,-117.705536+offset],\
                            [34.102840+offset,-117.705536+offset],\
                            [34.102840+offset,-117.705536-offset]])

def AllDiningCount(month, day, year, hour, minute):
    frary = 0
    frank = 0
    oldenborg = 0
    collins = 0
    malott = 0
    hoch = 0
    mcconnell = 0
    document_name = currentfile(month, day, year, hour, minute)
    with open(document_name, "r") as f:
        reader = csv.reader(f, delimiter=",")
        frary_b = mplPath.Path(frary_boundary)
        frank_b = mplPath.Path(frank_boundary)
        oldenborg_b = mplPath.Path(oldenborg_boundary)
        collins_b = mplPath.Path(collins_boundary)
        malott_b = mplPath.Path(malott_boundary)
        hoch_b = mplPath.Path(hoch_boundary)
        mcconnell_b = mplPath.Path(mcconnell_boundary)
        header = True
        for line in reader:
            if (header):
                header = False
                continue
            if (frary_b.contains_point((int(line[0]), int(line[1])))):
                frary+=1
            elif (frank_b.contains_point((int(line[0]), int(line[1])))):
                frank+=1
            elif (oldenborg_b.contains_point((int(line[0]), int(line[1])))):
                oldenborg+=1
            elif (collins_b.contains_point((int(line[0]), int(line[1])))):
                collins+=1
            elif (malott_b.contains_point((int(line[0]), int(line[1])))):
                malott+=1
            elif (hoch_b.contains_point((int(line[0]), int(line[1])))):
                hoch+=1
            elif (mcconnell_b.contains_point((int(line[0]), int(line[1])))):
                mcconnell+=1

    return [frary, frank, oldenborg, collins, malott, hoch, mcconnell]

""" Continuous implementation """
#for now, assume inputs are as follows:
#begin: 10-01-2017-00-00
#end: 10-31-2017-23-55
def prevDiningCount(month_begin, day_begin, year_begin, hour_begin, minute_begin, month_end, day_end, year_end, hour_end, minute_end):
    #initialize variables
    month = month_begin
    day = day_begin
    year = year_begin
    hour = hour_begin
    minute = minute_begin

    totalLife = [[],[],[],[],[],[],[]]

    #nested loop for days
    while (day != day_end):
        #reset hour
        hour = 0

        #nested loop for hours
        while (hour != 24):
            #reset minute
            minute = 0

            #nested loop for minutes
            while (minute != 60):
                if (month == month_end and day == day_end and year == year_end and hour == hour_end and minute == minute_end):
                    return totalLife
                # the actual calcuation call
                current = AllDiningCount(month, day, year, hour, minute)
                # update totalLife
                for i in totalLife:
                    totalLife[i]+=current[i]
                # update minute
                minute+=5
            # update hour
            hour+=1
        #update day
        day += 1

#main function that takes in commandline argument
def main():
	return 5

#playzone
#print fileLookup()
#print AllDiningCount(11, 10, 2017, 5, 35)
print prevDiningCount(10, 1, 2017, 0, 0, 10, 30, 2017, 23, 55)
