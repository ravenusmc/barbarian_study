#This file will contain the methods and class that will deal with all the data

#importing supporting libraries
import numpy as np
import pandas as pd

class Data():

    def __init__(self):
        self.data = pd.read_csv('./data/battle_data.csv')

    def basic_info(self):
        print(self.data.head())
        print(self.data.dtypes)

    def test(self):
        print(self.data[(self.data.Year >= -113) & (self.data.Year <= 28)])

obj = Data()
obj.basic_info()
obj.test()
