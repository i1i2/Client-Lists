#Client Lists Program

#fill lists
lastNameList  = ["Gumm", "Mann","Garden", "Dare", "Turner", "Friend", "Seek"]
firstNameList = ["Chuann", "Saad", "Rose", "Colin", "Paige", "Fiona", "Hayden"]
owedList      = [100, 0, 2000, 3500, 6000, 456, 10]
riskList      = []

#find the average 
def findAvg(owedList):
    avgOwed = 0
    total = 0
    totalCount = 0

    if len(owedList) > 0:
        totalCount = len(owedList)
        for item in owedList:
            total += item
        #end for
        if total > 0:
            avgOwed = total / totalCount
        else:
            avgOwed = 0
        #end if
    #end if
    return avgOwed
#end avgOwed

#find the maximum amount owed
def findMax(owedList):
    maxOwed = None
    positionMax = None
    if len(owedList) > 0:
        maxOwed = owedList[0]  # maxOwed = first item in list
        for item in owedList:
            if maxOwed < item:
                maxOwed = item
                positionMax = owedList.index(item) # get index value
            #end if
        #end for
    #end if
    return maxOwed, positionMax
#end findMax

#find the minimum amount owed
def findMin(owedList):
    minOwed = None
    positionMin = None
    if len(owedList) > 0:
        minOwed = owedList[0]  # minOwed = first item in list
        for item in owedList:
            if minOwed > item:
                minOwed = item
                positionMin = owedList.index(item) # get index value
            #end if
        #end for
    #end if
    return minOwed, positionMin
#end findMin

#get the risk
def getRisk(owedList):
	if len(owedList)>0:
		for index in range(len(owedList)):
			tempValue = owedList[index]
			if tempValue>=0 and tempValue < 100:
                				riskList.append("No Risk")
			elif tempValue >= 100 and  tempValue < 500:
				riskList.append("Low Risk")
			elif tempValue >= 500 and  tempValue < 1000:
				riskList.append("Medium Risk")
			else:
				riskList.append("High Risk")
			#end if  
        #end for
    #end if
	return riskList
#end riskList

#print results
def printResults(firstNameList, lastNameList, owedList, riskList, avgOwed, maxOwed, maxPostion, minOwed, minPosition):
    if len(firstNameList)>0:
        for index in range (len(firstNameList)):
            print (index, firstNameList[index], 
                   lastNameList[index], 
                   owedList[index],
                   riskList[index])
        #end for
        print()
        print ("Average amount owed : £", format(avgOwed, "6.2f"))
        client = firstNameList[positionMax] + " " + lastNameList[positionMax] 
        print (client,"owes Maximum Amount: £", format(maxOwed, "6.2f"))
        client = firstNameList[positionMin] + " " + lastNameList[positionMin] 
        print (client,"owes Minimum Amount: £", format(minOwed, "6.2f"))
    #end if
#end printResults

#main program
avgOwed = findAvg(owedList)
#find who owes the most money
maxOwed, positionMax  = findMax (owedList)
minOwed, positionMin  = findMin (owedList)
riskList = getRisk(owedList)
printResults(firstNameList, lastNameList, owedList, riskList, avgOwed, maxOwed, positionMax, minOwed, positionMin)
