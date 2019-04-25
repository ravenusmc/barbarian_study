#This file will clean the data and get the year column in the format that I want
#it in for this project.

#importing supporting libraries
import numpy as np
import pandas as pd

class Clean():

    def __init__(self):
        self.data = pd.read_csv('./data/battle_data.csv')

    def clean(self):
        for column in self.data.columns[0:1]:
            #print(self.data[column][0])
            phrase = self.data[column][0]
            #Checking for a dash in the years
            dash_location = phrase.find('-')
            print(dash_location)
            input()
            #Checking to see if the year is BCE or CE
            time_period_check_CE = phrase.find('A')
            time_period_check_BC = phrase.find('B')
            time_period_check_c = phrase.find('c')
            if dash_location != -1:
                if time_period_check_BC != -1:
                    year = int(phrase[0:dash_location])
                    #Turning the year negative
                    year = year * -1
                    print(year)
                elif time_period_check_CE != -1:
                    year = int(phrase[0:dash_location])
                    print(year)
                else:
                   year = int(phrase[0:dash_location])
                   print(year)
            else:
                if time_period_check_BC != -1:
                    #I don't want any white space in my answer so I'm subtracting one from
                    #the time period check.
                    stopping_value = time_period_check_BC - 1
                    year = int(phrase[0:stopping_value])
                    #Turning the year negative
                    year = year * -1
                    print(year)
                elif time_period_check_CE != -1:
                    #I don't want any white space in my answer so I'm subtracting one from
                    #the time period check.
                    stopping_value = time_period_check_CE - 1
                    year = int(phrase[0:stopping_value])
                    print(year)
                else:
                    num_list = []
                    for s in phrase:
                        if s.isdigit():
                            num_list.append(int(s))
                    print(num_list)
            print(year)
            input()

obj = Clean()
obj.clean()
