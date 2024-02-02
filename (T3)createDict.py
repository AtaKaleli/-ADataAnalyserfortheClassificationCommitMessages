import copy

nestedDict ={}
keysOFNames = {
    "SwM tasks":[0,0,0],
    "NFR Labeling":[0,0,0,0,0,0],
    "SoftEvol tasks":[0,0,0,0]
}
try:

    file = open("identifies.txt", "r")
    records = file.readlines()  # content of commit.txt file
    splittedList = []  # contains elements splitted with ","

    for data in records:
        data = data.split(",")
        splittedList.append(data)

    for item in splittedList:
        if item[1] in nestedDict.keys(): #item[1] has name  of the committer
            pass
        else:
            nestedDict[item[1]] = copy.deepcopy(keysOFNames)
            #I tried to directly assign the keyOFNames dictionary into nestedDict[nameOfCommitter],I figure out that
            #when I try to assign a value to specific key-value pair, for ex,nestedDict["Luca Bruno"]["SoftEvol tasks"][1] = 3
            #all of the softevol tasks values are changed for every committer. So I tried to use a copy of a keyOFNames dictionary,
            #but it also did not work. So I make a little researh and found the topic we also have seen in first weeks, which is
            #deepcopy. In this way, I prevent that nestedDict values are not point on same keysOfNames as values.

    nestedDict["Luca Bruno"]["SoftEvol tasks"][1] = 3
    print("key - value pairs:")
    for a,b in nestedDict.items():
        print(a,"-",b)


except:
    print("error")
