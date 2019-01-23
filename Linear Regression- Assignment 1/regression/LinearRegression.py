#!/usr/local/bin/python3
import numpy as np
import csv
import os

class LinearRegress():
    def __init__(self):
        print("constructor")
        self.readCsv()

    def readCsv(self):
        os.chdir('../dropbox/gitProjects/Machine Learning TDT4137/Linear Regression- Assignment 1/regression')
        cwd = os.getcwd()  # Get the current working directory (cwd)
        files = os.listdir(cwd)  # Get all the files in that directory
        print("Files in '%s': %s" % (cwd, files))

        with open("train_2d_reg_data.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                print(' '.join(row))



l1 = LinearRegress()
print("helo")
