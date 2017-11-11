import os
import numpy as np
import csv
import matplotlib.path as mplPath

#format: quadralateral (x1, y1, x2, y2,...) corresponding to the four corners
frary_2d = np.array([1, 1, 2, 5, 6, 6, 5, 0])

#function returns how many people are at frary at a certain time
def fraryCount():
	with open('tues_11_10_2017_5_35.csv', 'rb') as csvfile:
		has_header = csv.Sniffer().has_header(inf.read(1024))
		reader = csv.reader(csvfile, delimiter=",")
		if (has_header):
			next(reader)
		counter = 0
		boundary = mplPath.Path(np.array([frary_2d[0]]))
		for row in reader:
			if (boundary.contains_point((int(row[0]), int(row[1])))):
				counter+=1

	csvfile.close()
	return counter

def timeEstimate():


def main():
	




print fraryCount()