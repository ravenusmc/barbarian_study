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
        #print(self.data.Result.unique())

    # def test(self):
    #     print(self.data[(self.data.Year >= -113) & (self.data.Year <= 28)])

    def buildColorChart(self, yearOne, yearTwo):
        #This list will hold all of the distinct Roman Victories.
        roman_victories = ['Decisive Roman victory', 'Roman victory',
         'Roman victory (according to Tacitus)',
         'Decisive Eastern Roman victory', 'Minor Roman victory',
         'Roman/Suevi victory', 'Roman-Hunnic victory',
         'Visigothic/Roman victory','Decisive Byzantine victory',
         'Byzantine victory']
        time_frame_data_set = self.data[(self.data.Year >= yearOne) & (self.data.Year <= yearTwo)]
        data_set_length = len(time_frame_data_set)
        count = 0
        for victory in roman_victories:
            data_set = time_frame_data_set[(time_frame_data_set.Result == victory)]
            number_of_victories = len(data_set)
            count = number_of_victories + count
        data = {}
        data['Total'] = int(data_set_length)
        data['Roman_Victories'] = int(count)
        return data

    def build_Chart_One(self):
        start_year = -113
        #This list will hold all of the distinct Roman Victories.
        roman_victories = ['Decisive Roman victory', 'Roman victory',
         'Roman victory (according to Tacitus)',
         'Decisive Eastern Roman victory', 'Minor Roman victory',
         'Roman/Suevi victory', 'Roman-Hunnic victory',
         'Visigothic/Roman victory','Decisive Byzantine victory',
         'Byzantine victory']
        graphOneData = []
        #This will keep track of each interval of 75 year period
        interval = 1
        while start_year <= 569:
            sub_data = {}
            interval_year = start_year + 75
            time_frame_data_set = self.data[(self.data.Year >= start_year) & (self.data.Year <= interval_year)]
            #Working on getting the number of roman victories in time frame
            data_set_length = len(time_frame_data_set)
            count = 0
            for victory in roman_victories:
                data_set = time_frame_data_set[(time_frame_data_set.Result == victory)]
                number_of_victories = len(data_set)
                count = number_of_victories + count
            year_interval = str(start_year) + ' to ' + str(interval_year)
            sub_data['Interval'] = interval
            sub_data['Year Interval']  = year_interval
            sub_data['Total Battles'] = int(data_set_length)
            sub_data['Roman Victories'] = int(count)
            #I have to increase the interval of start year so I'm not stuck in
            #the loop forever
            start_year = start_year + 75
            sub_data['Count'] = count
            interval += 1
            graphOneData.append(sub_data)
        return graphOneData



obj = Data()
# obj.basic_info()
# obj.test()
obj.build_Chart_One()

#Distinct result column names from where Romans one battles.
# 'Decisive Roman victory', 'Roman victory'
#  'Roman victory (according to Tacitus)'
#  'Decisive Eastern Roman victory' 'Minor Roman victory'
#  'Roman/Suevi victory' 'Roman-Hunnic victory'
#  'Visigothic/Roman victory'
#  'Decisive Byzantine victory' 'Byzantine victory'
