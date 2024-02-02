import re
import copy



#dictionary creation
IDsDict ={} #this dictionary hold key-value pairs as commiterName-ID(s)
nestedDict ={} #the nested dictionary
keysOFNames = {
    "SwM tasks":[0,0,0],
    "NFR Labeling":[0,0,0,0,0,0],
    "SoftEvol tasks":[0,0,0,0]
}

file = open("identifies.txt", "r")
records = file.readlines()  # content of commit.txt file
splittedList = []  # contains elements splitted with ","

for data in records[1:]:#I ignore the first line of the txt, because it is just "Commiter ID,Full Name,eMail"
    data = data.split(",")
    splittedList.append(data)


for item in splittedList:
    if item[1] in nestedDict.keys():  # item[1] has name  of the committer
        pass
    else:
        nestedDict[item[1]] = copy.deepcopy(keysOFNames)


#IDsDict
for item in splittedList:
    if item[1] in IDsDict.keys():  # item[1] has name  of the committer
        pass
    else:
        IDsDict[item[1]] = []

for key,value in IDsDict.items(): #assign ids with commiter names
    for item in splittedList:
        if item[1] == key:
            value.append(item[0])


file.close()

#get classification values
file = open("commits.txt","r")
strippedList = []  # contains file content without " \n "
records = file.readlines()  # content of commit.txt file
noOfCommits = 0  # number of commits (count of the lines)

for record in records[1:]:#same ignorance like identifies.txt, I ignore the first line of commits.txt data
    rec = record.strip()
    strippedList.append(rec)
    noOfCommits += 1

splittedList = []  # contains elements splitted with ","

for data in strippedList:
    data = data.split(",")
    splittedList.append(data)

CCF = []  # contains only commit classification features and committerID  (range of 2-15 of data)

for i in range(noOfCommits):
    CCF.append(splittedList[i][1:15])  # take data of splittedList, from index range 1:1

for query in CCF:
    query = "".join(query)
    pattern = re.match("(\d{3})(\d{6})(\d{4})(\d+)", query).groups()
    for key,value in IDsDict.items():
        if pattern[3] in value:
            for i in range(3):  # for swm
                nestedDict[key]["SwM tasks"][i] += int(pattern[0][i])
            for i in range(6):  # for nfr
                nestedDict[key]["NFR Labeling"][i] += int(pattern[1][i])
            for i in range(4):  # for soft
                nestedDict[key]["SoftEvol tasks"][i] += int(pattern[2][i])

file.close()

print("key - value pairs:")
for key,value in nestedDict.items():
    print(key,"-",value)





