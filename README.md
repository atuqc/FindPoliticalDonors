# Table of Contents
1. [Introduction](README.md#introduction)

# Introduction
Python 2.7 was used to complete this challenge
main.py is the pyhton file containing the source code
within this file I have created several functions to solve the challenge problem
The main data structure used is a nested dictionary. 
In the zipcode case,the outer key is a zip code and the value is a dictionary whose key is the CMTE_ID, the value of which is a list of contributions for that CMTE_ID in that zipcode
Similarly in the date case, the outer key is a date and the value is a dictionary whose key is the CMTE_ID, the value of which is a list of contributions for that CMTE_ID in that date

- isValidDate(someDate)

checks if someDate field is empty and/or malformed (i.e has less than 5 digits or contains a letter)

- isValidZip(someZip)

checks if someZip field is empty and/or malformed (i.e has less than 5 digits or contains a letter)

- isValueNumber(someValue)

checks if someValue is a string containing numbers only

- getRunningMedian(currentLines,zipcode,output)

Calculates median for contributions as they come in based in zipcode( in this case as next line is read) by iterating thorugh the nested dictionary.

- writeData(x,filename)

writes x into file named filename

- readDataStream(someInput,output)

reads file one by one and populates nested dictionary accordingly,
after adding new entry or updating an entry the dectionary is sent to getRunningMedian to calculate current median

- calcMedian(someList):

calculates median of someList(list contains floats)

- getMedianByDate(lines)

iterates through lines dictionary to generate list containing lines to be written into by date output


