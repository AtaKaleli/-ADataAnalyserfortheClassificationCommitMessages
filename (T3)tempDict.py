

nestedDict ={}
keysOFNames = {
    "SwM tasks":[0,0,0],
    "NFR Labeling":[0,0,0,0,0,0],
    "SoftEvol tasks":[0,0,0,0]
}

namesDictionaryHolder = []
namesDictionaryHolder.append(keysOFNames) # initially contains keyOfNames dictionary


try:

    file = open("identifies.txt", "r")
    records = file.readlines()  # content of commit.txt file
    splittedList = []  # contains elements splitted with ","
    count = 0 #count of committers
    for data in records:
        data = data.split(",")
        splittedList.append(data)

    for item in splittedList:
        if item[1] in nestedDict.keys(): #item[1] has name  of the committer
            pass
        else:
            nestedDict[item[1]] = namesDictionaryHolder[count]
            namesDictionaryHolder.append(keysOFNames)
            count+=1

    nestedDict["Luca Bruno"]["SoftEvol tasks"][1] = 3
    print("key - value pairs:")
    for a,b in nestedDict.items():
        print(a,"-",b)


except:
    print("error")
