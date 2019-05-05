#This file will contain the methods and class that will deal with all the data

#importing supporting libraries
import numpy as np
import pandas as pd

class Data():

    def __init__(self):
        self.data = pd.read_csv('./data/battle_data.csv')

    # def basic_info(self):
    #     print(self.data.head())
    #     print(self.data.dtypes)

    def test(self):
        print(self.data[(self.data.Year >= -113) & (self.data.Year <= 28)])

    def buildColorChart(self, yearOne, yearTwo):
        new_data = self.data[(self.data.Year >= yearOne) & (self.data.Year <= yearTwo)]
        data_set_length = len(new_data)
        print(self.data.Result.unique())
        return data_set_length

# obj = Data()
# obj.basic_info()
# obj.test()

'Decisive Roman victory', 'Roman victory'
 'Roman victory (according to Tacitus)'
 'Decisive Eastern Roman victory' 'Minor Roman victory'
 'Roman/Suevi victory' 'Roman-Hunnic victory'
 'Visigothic/Roman victory'
 'Decisive Byzantine victory' 'Byzantine victory'
