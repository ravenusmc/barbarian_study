#This is where the web scraping will occur. The site that will be scraped
#is the following: https://en.wikipedia.org/wiki/List_of_the_Germanic_Wars

#Importing libraries that will be used in this project.
from bs4 import BeautifulSoup
from csv import writer
import requests

#This class will take care of all of the scraping
class Scraping():

    def __init__(self):
        self.requests = "https://en.wikipedia.org/wiki/List_of_the_Germanic_Wars"

    #This method will set up the initial url
    def setup_soup(self):
        self.response = requests.get(self.requests)
        #setting up beautiful soup.
        self.soup = BeautifulSoup(self.response.text, "html.parser")


    def build_csv_file(self):
        #opening up the csv file that I'll write to
        with open("battle_data.csv", "w") as csv_file:
            #Creating a csv variable
            csv_writer = writer(csv_file)
            #This line will write the rows to the CSV file, the header rows.
            csv_writer.writerow(["Mod_Year", "Orig_Year", "Name", "Location", "Belligerent_1", "Belligerent_2", "Result"])
            #Getting the table from the wikipedia page
            table = self.soup.find('table', {'class':'wikitable'})
            #Looping through each row to get all of the data
            for row in table.find_all('tr'):
                #grabbing each row of data
                columns = row.find_all('td')
                #This list will hold each rows data points which will be used to
                #build the csv
                data_list = []
                for column in columns:
                    #Getting the actual text out of the html
                    column_data = str(column.get_text().replace('\n', ""))
                    #This process here will start working to convert the date to
                    #a format that I can work with.
                    #Checking for a dash in the years
                    dash_location = column_data.find('–')
                    ##Checking to see if the date is BC, AD or C.
                    time_period_check_CE = column_data.find('AD')
                    time_period_check_BC = column_data.find('BC')
                    time_period_check_c = column_data.find('c.')
                    if dash_location != -1:
                        if time_period_check_BC != -1:
                            year = int(column_data[0:dash_location])
                            #Turning the year negative
                            year = year * -1
                            data_list.append(int(year))
                        elif time_period_check_CE != -1:
                            year = int(column_data[0:dash_location])
                            data_list.append(int(year))
                        else:
                           year = int(column_data[0:dash_location])
                           data_list.append(int(year))
                    else:
                        # print(column_data)
                        # print(time_period_check_CE)
                        # print(time_period_check_BC)
                        # print(time_period_check_c)
                        # input()
                        if time_period_check_BC != -1:
                            #I don't want any white space in my answer so I'm subtracting one from
                            #the time period check.
                            stopping_value = time_period_check_BC - 1
                            year = int(column_data[0:stopping_value])
                            #Turning the year negative
                            year = year * -1
                            data_list.append(int(year))
                        elif time_period_check_CE != -1:
                            #I don't want any white space in my answer so I'm subtracting one from
                            #the time period check.
                            stopping_value = time_period_check_CE - 1
                            year = int(column_data[0:stopping_value])
                            data_list.append(int(year))
                        elif time_period_check_c != -1:
                            num_list = []
                            for s in column_data:
                                if s.isdigit():
                                    num_list.append(s)
                            year = "".join(num_list)
                            data_list.append(int(year))
                        # else:
                        #     data_list.append(column_data)
                    #adding each column to the list.
                    data_list.append(column_data)
                #This will ensure that only list that have data are inserted
                #into the csv file.
                if data_list:
                    #Adding each list that's built to the csv
                    csv_writer.writerow(data_list)

scrape = Scraping()
scrape.setup_soup()
scrape.build_csv_file()
