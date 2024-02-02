import re
import copy

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

for data in records:
    data = data.split(",")
    splittedList.append(data)

for item in splittedList:
    if item[1] in nestedDict.keys():  # item[1] has name  of the committer
        pass
    else:
        nestedDict[item[1]] = copy.deepcopy(keysOFNames)

# nested list initial version
# print("key - value pairs:")
# for a,b in nestedDict.items():
#     print(a,"-",b)

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
# commiterName -ID pair
# for key,value in IDsDict.items():
#     print(key,"-",value)





# query = ['0','1','0','0','1','1','0','0','0','0','0','1','0','5']
# query = "".join(query)
# pattern = re.match("(\d{3})(\d{6})(\d{4})(\d+)",query).groups()
#
#
# for key,value in IDsDict.items():
#     if pattern[3] in value:
#         for i in range(3):  # for swm
#             nestedDict[key]["SwM tasks"][i] += int(pattern[0][i])
#         for i in range(6):  # for nfr
#             nestedDict[key]["NFR Labeling"][i] += int(pattern[1][i])
#         for i in range(4):  # for soft
#             nestedDict[key]["SoftEvol tasks"][i] += int(pattern[2][i])

queries = [ ['0','1','0','0','1','1','0','0','0','0','0','1','0','16'],
            ['0','1','0','0','0','1','0','0','0','0','0','1','0','3']
          ]


for query in queries:
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



print("key - value pairs:")
for key,value in nestedDict.items():
    print(key,"-",value)




