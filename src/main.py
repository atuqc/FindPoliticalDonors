def isValidDate(someDate):
    #check if date is valid
    num = isValueNumber(someDate)
    if someDate and len(someDate)>=8 and num:
        return True
    else:
        return False
    
def isValidZip(someZip):
    #check if zipcode is valid
    num = isValueNumber(someZip)
    if someZip and len(someZip)>=5 and num:
        return True
    else:
        return False
def isValueNumber(someValue):
    try:
        int(someValue)
        return True
    except:
        return False
    
def getRunningMedian(currentLines,zipcode,output):
    #calculate mean as lines come in
    count = 0
    totalsum = 0
    median = 0
    data = currentLines[zipcode]
    amountList = [] #list contains contributions so far
    for ID in data:
        for lineList in data[ID]:
            totalsum += float(lineList[14])
            amountList.append(float(lineList[14]))
            count += 1
        totalsum = int(totalsum)
        median = calcMedian(amountList) #median is calculated with contributions so far
        myLine = ID +'|'+ zipcode +'|'+ str(median) + '|'+ str(count) + '|' + str(totalsum)+'\n'
        writeData(myLine,output)
        
    
def writeData(x,filename):
    myfile = open(filename,'a+')
    myfile.write(x)
    myfile.close()

def readDataStream(someInput,output):
    mainList=[]
    currentLines = {}
    idDict = {}
    with open(someInput) as stream:
        for line in stream:
            tempLine = str.rstrip(line,'\n')
            tempLine = str.split(tempLine,'|')
            mainList.append(tempLine)
            if isValidZip(tempLine[10]) and not tempLine[15]:
                if tempLine[10][0:5] in currentLines:
                    temp = currentLines[tempLine[10][0:5]]
                    if tempLine[0] in temp:
                        temp[tempLine[0]].append(tempLine)
                        currentLines[tempLine[10][0:5]]=temp
                        getRunningMedian(currentLines,tempLine[10][0:5],output)
                    else:
                        temp[tempLine[0]] = [tempLine]
                        currentLines[tempLine[10][0:5]]=temp
                        getRunningMedian(currentLines,tempLine[10][0:5],output)
                else:
                    temp ={}
                    temp[tempLine[0]]=[tempLine]
                    currentLines[tempLine[10][0:5]] = temp
                    getRunningMedian(currentLines,tempLine[10][0:5],output)
            #print (len(tempLine))
    stream.close()
    return mainList

def calcMedian(someList):
    sortList = sorted(someList)
    median = 0
    index = len(someList)//2
    if len(someList)%2 == 1:
        median = int(sortList[index])
    else:
        median = int(round((sortList[index-1]+sortList[index])/2))
    return median
def getMedianByDate(lines):
    listLine = []
    for date in lines:
        for ID in lines[date]:
            totalsum = 0
            median = 0
            amountlist = []
            count = 0
            for j in lines[date][ID]:
                amountlist.append(float(j[14]))
                totalsum += float(j[14])
                count+=1
                totalsum = int(totalsum)
                median = calcMedian(amountlist)
            newline = j[0]+'|'+ j[13]+'|'+ str(median) + '|'+ str(count) + '|' + str(totalsum)+'\n'
            listLine.append(newline)
    return sorted(listLine)
outputFileA = "./output/medianvals_by_zip.txt"
outputFileB ="./output/medianvals_by_date.txt"
inputFile = "./input/intcont.txt"
mainList = readDataStream(inputFile,outputFileA) #file is read line by line
# list of lines is returned to process by date later

#Lines are processed by Date
currentDates = {} 
for j in mainList:
    if isValidDate(j[13]) and not j[15]:
        if j[13] in currentDates:
            temp = currentDates[j[13]]
            if j[0] in temp:
                temp[j[0]].append(j)
                currentDates[j[13]]=temp
            else:
                temp[j[0]] = [j]
                currentDates[j[13]] = temp               
        else:
            temp = {}
            temp[j[0]] = [j]
            currentDates[j[13]] = temp

dateLines = getMedianByDate(currentDates)           
for i in dateLines:
    writeData(i,outputFileB)

print ("Process Finished  j")
