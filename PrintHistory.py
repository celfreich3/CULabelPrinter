#Imports
import datetime
import time
import csv
import os

#On direct file execution
if __name__ == "__main__":
    #Print greeting and instructions
    os.system('CLS')
    print("Welcome to the product label history viewer!\n")
    #Capture date and convert to datetime
    searchDate = datetime.datetime.strptime(input("Please enter a day in the format MM/DD/YYYY to view it's print history: \n"), "%m/%d/%Y")

    #Open CSV
    with open("history.csv") as csvfile:
        #Check each entry for the same date as user input
        for entry in csv.reader(csvfile):
            epoch = datetime.datetime.fromtimestamp(int(entry[0]))
            if epoch.date() == searchDate.date():
                #Print out product name and product weight
                print("P: " + entry[1] + " W: " + entry[2])

