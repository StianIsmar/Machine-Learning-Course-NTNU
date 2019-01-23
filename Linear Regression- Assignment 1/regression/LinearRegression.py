#!/usr/local/bin/python3
import csv
import numpy as np
import os

class LinearRegress():
    def __init__(self):
        print("constructor")
        self.constructMatrix()
        self.readCsv()

    def constructMatrix(self):
        print("make the three matrix")

    def readCsv(self):
        os.chdir('../regression')
        print("dir")
        cwd = os.getcwd()  # Get the current working directory (cwd)
        files = os.listdir(cwd)  # Get all the files in that directory
        print("Files in '%s': %s" % (cwd, files))

        with open("train_2d_reg_data.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                print(' '.join(row))




l1 = LinearRegress()
