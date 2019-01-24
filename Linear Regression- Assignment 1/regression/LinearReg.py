#!/usr/local/bin/python3
import csv
import numpy as np
import os

class LinearRegress():
    def __init__(self):
        self.readCsv()

    def readCsv(self):

        data = np.loadtxt('train_1d_reg_data.csv', delimiter=',', skiprows=1, unpack=False)
        print(len(data), "datalen")
# All data in the first column (x)
        x = data[..., 0]

# All data in the second column (y)
        y = data[..., 1]
        print(data)
        print(x)



l1 = LinearRegress()