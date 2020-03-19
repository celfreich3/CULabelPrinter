#Imports
import datetime
import time
import os
from shutil import copyfile

#Global variable declerations
templateText = ""
productName = ""
productWeight = ""

def loadTemplate(file):
    #Open the template file and return its data
    f = open(file, "r")
    return f.read()

def formatLabel():
    #Create a copy of the template data
    newLabel = templateText

    #Find and replace parameters with user inputs and date
    newLabel = newLabel.replace("{productName}", productName)
    newLabel = newLabel.replace("{productWeight}", productWeight)
    newLabel = newLabel.replace("{date}", datetime.date.today().strftime("%m/%d/%Y"))

    #Pass label data to be printed
    printLabel(newLabel)

def printLabel(label):
    #Write the label to a text file that can be copied onto the printer
    print("\nCreating label...\n")
    filePath = os.getcwd() + "\label.txt"
    with open(filePath, "w") as fp:
        fp.write(label)

    #Copy the newly written label to the zebra printer
    #The printer can be found at \\{ComputerName}\{PrinterSharedName}
    print("Printing...\n")
    copyfile(filePath, "\\\\" + os.environ['COMPUTERNAME'] + "\ZPL")

    #Save the print job to a csv that uses epoch as UUID
    filePath = os.getcwd() + "\history.csv"
    with open(filePath, "a") as fp:
        fp.write(str(int(time.time())) + "," + productName + "," + productWeight + "\n")

    #Loop back to collect input for another print job
    collectInput()

def collectInput():

    #Grab global variables to be updated
    global productName
    global productWeight

    #Collect Product Name and Weight and check for special input cases
    newProductName = input("Enter product name: \n")

    #Special input cases: -1 is exit code, $ is repeate previous input for variable
    if newProductName == "-1":
        shutDown()
    elif newProductName != "$":
        productName = newProductName


    newProductWeight = input("Enter product weight: \n")

    if newProductWeight == "-1":
        shutDown()
    elif newProductWeight != "$":
        productWeight = newProductWeight

    #Call label format process
    formatLabel()

def shutDown():
    #Print a message and shutdown execution
    print("Shutting down the program... Thank you!")
    exit()

#On direct file execution
if __name__ == "__main__":
    
    #Print greeting and instructions
    os.system('CLS')
    print("Welcome to the product label generator!\n")
    print("At any time enter '$' to use a previous response to a question.\n")
    print("To exit the program at any time enter '-1'\n\n")

    #Save template
    templateText = loadTemplate("template.txt")

    #Enter input loop execution
    collectInput()
