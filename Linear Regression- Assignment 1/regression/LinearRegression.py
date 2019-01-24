#!/usr/local/bin/python3
import csv
import numpy as np
import os

class LinearRegress():
    def __init__(self):
        print("constructor")
        dataArray, numOfObs = self.readCsv()
        self.constructMatrix(dataArray, numOfObs)

    def readCsv(self):
        os.chdir('../regression')
        cwd = os.getcwd()  # Get the current working directory (cwd)
        files = os.listdir(cwd)  # Get all the files in that directory
        # print("Files in '%s': %s" % (cwd, files))
        # Lenth of csv file!! store it somewhere

        with open("train_2d_reg_data.csv") as f:
            reader = csv.reader(f)
            counter = 0
            dataArray = []
            for row in reader:
                # print(' '.join(row))
                dataArray.append(row)
                # print(row)
                # matrix = np.concatenate((matrix, row))
                # print(row)
                counter += 1
            # print(matrix)
            # number of observations in the CSV-file.
            counter = counter - 1
            print(counter, "COUNTEREND")

        return dataArray, counter


    def constructMatrix(self, dataArray, numOfObs):
        # print(numOfObs) # 325 rows of observations!
        dataArray = np.delete(dataArray, 0, axis = 0 )
        # M has numOfObs rows and 3 columns!
        M = np.ones((numOfObs, 3))
        # print(M)

        # X has numOfObs rows and 3 columns!
        X = np.zeros((numOfObs, 3))
        # print (X)

        # Y is just 1-d array:
        Y = np.zeros([],dtype=int)

        # Filling M, X and Y with the actual data from the CSV:
        # **** Y:
        for obs in dataArray:
            Y = np.append(Y, obs[2])
        # Remove the two first elements, they should not be there:
        Y =  np.delete(Y,0)
        # *** M: Should have 3 columns, with each having row 1,x1,x2:
        print
        for obs in dataArray:
            print(obs)
            for row in range(0, len(M)):
                for col in range(1,3):
                    print(M[row,col])
                    M[row,col] = obs[(col-1)]
        print(M)
        print(M[0,1])







            # Y = np.append(Y, obs[2])
            # print(Y)
            # print(len(dataArray))
            # print(len(Y))

l1 = LinearRegress()