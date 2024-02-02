try:
    file = open("commits.txt","r")
    strippedList = [] #contains file content without " \n "
    records = file.readlines() #content of commit.txt file
    noOfCommits=0 #number of commits (count of the lines)

    for record in records:
        rec = record.strip()
        strippedList.append(rec)
        noOfCommits+=1

    splittedList = [] #contains elements splitted with ","

    for data in strippedList:
        data = data.split(",")
        splittedList.append(data)

    CCF = [] #contains only commit classification features and committerID  (range of 2-15 of data)

    for i in range(noOfCommits):
        CCF.append(splittedList[i][1:15]) # take data of splittedList, from index range 1:1

    for item in CCF:
        print(item)
except:
    print("File could not be opened!")