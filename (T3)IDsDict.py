IDsDict ={} #this dictionary hold key-value pairs as commiterName-ID(s)

file = open("identifies.txt", "r")
records = file.readlines()  # content of commit.txt file
splittedList = []  # contains elements splitted with ","

for data in records:
    data = data.split(",")
    splittedList.append(data)

for item in splittedList:
    if item[1] in IDsDict.keys():  # item[1] has name  of the committer
        pass
    else:
        IDsDict[item[1]] = []

for key,value in IDsDict.items(): #assign ids with commiter names
    for item in splittedList:
        if item[1] == key:
            value.append(item[0])

for key,value in IDsDict.items():
    print(key,"-",value)

value='3' #get the name of the commiter using  ID

for a,b in IDsDict.items():
    if value in b:
        print(a)





