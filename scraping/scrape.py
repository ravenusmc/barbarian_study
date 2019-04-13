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
            csv_writer.writerow(["Year", "Name", "Location", "Belligerent_1", "Belligerent_2", "Result"])
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
                    column_data = column.get_text().replace('\n', '')
                    #adding each column to the list.
                    data_list.append(column_data)
                #This will ensure that only list that have data are inserted
                #into the csv file.
                if data_list:
                    #Adding each list that's built to the csv
                    csv_writer.writerow(data_list)

# scrape = Scraping()
# scrape.setup_soup()
# scrape.build_csv_file()
