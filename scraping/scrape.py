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


    def push_into_csv(self):
        #opening up the csv file that I'll write to
        with open("battle_data.csv", "w") as csv_file:
            #Creating a csv variable
            csv_writer = writer(csv_file)
            #This line will write the rows to the CSV file, the header rows.
            csv_writer.writerow(["Year", "Name", "Location", "Belligerents", "Result"])
            #Getting the table from the wikipedia page
            table = self.soup.find('table', {'class':'wikitable'})
            row_marker = 0
            #Looping through each row to get all of the data
            for row in table.find_all('tr'):
                column_marker = 0
                columns = row.find_all('td')
                print(columns)
                input()

                #csv_writer.writerow([year, total, black, jewish, islamic])
                # for column in columns:
                #     new_table.iat[row_marker,column_marker] = column.get_text()
                #     column_marker += 1

scrape = Scraping()
scrape.setup_soup()
scrape.push_into_csv()
