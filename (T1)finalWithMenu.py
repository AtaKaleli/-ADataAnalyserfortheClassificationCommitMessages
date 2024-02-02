import re
import copy
import matplotlib.pyplot as plt

def menu():
    print("\n1. Compare the number of commits done by a particular developer")
    print("2. Compare the number of commits done by all developers")
    print("3. Print the developer with the maximum number of commits")
    print("4. Exit")

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
    print(pattern)
    for key,value in IDsDict.items():
        if pattern[3] in value:
            for i in range(3):  # for swm
                nestedDict[key]["SwM tasks"][i] += int(pattern[0][i])
            for i in range(6):  # for nfr
                nestedDict[key]["NFR Labeling"][i] += int(pattern[1][i])
            for i in range(4):  # for soft
                nestedDict[key]["SoftEvol tasks"][i] += int(pattern[2][i])

file.close()

# print("key - value pairs:")
# for key,value in nestedDict.items():
#     print(key,"-",value)



while(True):#this loop continue until user enter 4 as an option.
    menu()
    option = int(input("Please enter an option between 1-4: "))

    if(option == 1):
        #lists available classifications
        print("\nAvailable classification schemes are as follows: ")
        print("Swanson's Maintenance Tasks (SwM)")
        print("NFR Labeling")
        print("Software Evolution Tasks (SoftEvol)")

        #list available committers
        print("\nAvailable Committers are as follows: ")
        for key in IDsDict.keys():
            print(key)

        classificationScheme = input("\nPlease enter classification scheme: ")
        #invalid classificationScheme control
        while(classificationScheme != "Swanson's Maintenance Tasks" and classificationScheme != "SwM" and classificationScheme != "NFR Labeling" and classificationScheme != "Software Evolution Tasks" and classificationScheme != "SoftEvol" ):
            print("You entered invalid classificationScheme! ")
            classificationScheme = input("\nPlease enter classification scheme: ")


        committerNames = [] #names list for error check
        for key in IDsDict.keys():
            committerNames.append(key)

        committer = input("Please enter committer name: ")

        #invalid committer control
        while(committer not in committerNames):
            print("You entered invalid committer! ")
            committer = input("Please enter committer name: ")

        if(classificationScheme == "Swanson's Maintenance Tasks" or classificationScheme == "SwM"):
            classificationScheme = "SwM tasks" # I assign classificationScheme as SwM tasks as I used this string when I create the nested dictionary's values part (keysOfNames)
            features = ["Adaptive Tasks", "Corrective Tasks", "Perfective Tasks"] # features of SwM tasks
            values = [] #values of SwM tasks

            for i in range(3):
                values.append(nestedDict[committer][classificationScheme][i])

        elif(classificationScheme == "NFR Labeling"):
            features = ["Maintainability", "Usability", "Functionality","Reliability", "Efficiency", "Portability"]  # features of NFR Labeling
            values = []  # values of NFR Labeling tasks

            for i in range(6):
                values.append(nestedDict[committer][classificationScheme][i])

        elif(classificationScheme == "Software Evolution Tasks" or classificationScheme == "SoftEvol"):
            classificationScheme = "SoftEvol tasks"  # I assign classificationScheme as SoftEvol tasks as I used this string when I create the nested dictionary's values part (keysOfNames)
            features = ["Forward Engineering", "Re-Engineering", "Corrective Engineering", "Management"]  # features of Software Evolution Tasks
            values = []  # values of Software Evolution Tasks

            for i in range(4):
                values.append(nestedDict[committer][classificationScheme][i])

        #bar chart visualisation
        plt.bar(features, values)
        plt.xlabel('Features')
        plt.ylabel('Total Number of Commits')
        plt.title("Comparison for " + committer + " Commits Classified by " + classificationScheme)
        plt.show()

    elif(option == 2):
        # lists available classifications
        print("\nAvailable classification schemes are as follows: ")
        print("Swanson's Maintenance Tasks (SwM)")
        print("NFR Labeling")
        print("Software Evolution Tasks (SoftEvol)")
        classificationScheme = input("\nPlease enter classification scheme: ")

        # invalid classificationScheme control
        while (classificationScheme != "Swanson's Maintenance Tasks" and classificationScheme != "SwM" and classificationScheme != "NFR Labeling" and classificationScheme != "Software Evolution Tasks" and classificationScheme != "SoftEvol"):
            print("You entered invalid classificationScheme! ")
            classificationScheme = input("\nPlease enter classification scheme: ")

        if (classificationScheme == "Swanson's Maintenance Tasks" or classificationScheme == "SwM"):
            classificationScheme = "SwM tasks"  # I assign classificationScheme as SwM tasks as I used this string when I create the nested dictionary's values part (keysOfNames)

            # lists available classifications
            print("\nCorresponding features of SwM tasks are as follows: ")
            print("Adaptive Tasks")
            print("Corrective Tasks")
            print("Perfective Tasks")

            correspondingFeature = input("\nPlease enter the corresponding feature: ")

            # invalid correspondingFeature control
            while (correspondingFeature != "Adaptive Tasks" and correspondingFeature != "Corrective Tasks" and correspondingFeature != "Perfective Tasks"):
                print("You entered invalid correspondingFeature! ")
                correspondingFeature = input("\nPlease enter corresponding feature: ")

            #assign indexes to get values from dictionary using these indexes
            if(correspondingFeature == "Adaptive Tasks"):
                index = 0
            elif(correspondingFeature == "Corrective Tasks"):
                index = 1
            elif(correspondingFeature == "Perfective Tasks"):
                index = 2

            features = [] #filled with commiter names
            values = []  # filled with correspoding feature values
            for key in IDsDict.keys():
                features.append(key)
                values.append(nestedDict[key][classificationScheme][index])

        elif (classificationScheme == "NFR Labeling"):
            # lists available classifications
            print("\nCorresponding features of NFR Labeling are as follows: ")
            print("Maintainability")
            print("Usability")
            print("Functionality")
            print("Reliability")
            print("Efficiency")
            print("Portability")

            correspondingFeature = input("\nPlease enter the corresponding feature: ")

            # invalid correspondingFeature control
            while (correspondingFeature != "Maintainability" and correspondingFeature != "Usability" and correspondingFeature != "Functionality" and correspondingFeature != "Reliability" and correspondingFeature != "Efficiency" and correspondingFeature != "Portability"):
                print("You entered invalid correspondingFeature! ")
                correspondingFeature = input("\nPlease enter corresponding feature: ")

            # assign indexes to get values from dictionary using these indexes
            if (correspondingFeature == "Maintainability"):
                index = 0
            elif (correspondingFeature == "Usability"):
                index = 1
            elif (correspondingFeature == "Functionality"):
                index = 2
            elif (correspondingFeature == "Reliability"):
                index = 3
            elif (correspondingFeature == "Efficiency"):
                index = 4
            elif (correspondingFeature == "Portability"):
                index = 5


            features = []  # filled with commiter names
            values = []  # filled with correspoding feature values
            for key in IDsDict.keys():
                features.append(key)
                values.append(nestedDict[key][classificationScheme][index])

        elif (classificationScheme == "Software Evolution Tasks" or classificationScheme == "SoftEvol"):
            classificationScheme = "SoftEvol tasks"  # I assign classificationScheme as SoftEvol tasks as I used this string when I create the nested dictionary's values part (keysOfNames)
            # lists available classifications
            print("\nCorresponding features of NFR Labeling are as follows: ")
            print("Forward Engineering")
            print("Re-Engineering")
            print("Corrective Engineering")
            print("Management")

            correspondingFeature = input("\nPlease enter the corresponding feature: ")

            # invalid correspondingFeature control
            while (correspondingFeature != "Forward Engineering" and correspondingFeature != "Re-Engineering" and correspondingFeature != "Corrective Engineering" and correspondingFeature != "Management"):
                print("You entered invalid correspondingFeature! ")
                correspondingFeature = input("\nPlease enter corresponding feature: ")

            # assign indexes to get values from dictionary using these indexes
            if (correspondingFeature == "Forward Engineering"):
                index = 0
            elif (correspondingFeature == "Re-Engineering"):
                index = 1
            elif (correspondingFeature == "Corrective Engineering"):
                index = 2
            elif (correspondingFeature == "Management"):
                index = 3


            features = []  # filled with commiter names
            values = []  # filled with correspoding feature values
            for key in IDsDict.keys():
                features.append(key)
                values.append(nestedDict[key][classificationScheme][index])

        # bar chart visualisation
        plt.bar(features, values)
        plt.xlabel('Features')
        plt.ylabel('Total Number of Commits')
        plt.title("Comparison of all " + classificationScheme + "done by all developers with the feature of " + correspondingFeature)
        plt.show()

    elif(option == 3):
        # lists available classifications
        print("\nAvailable classification schemes are as follows: ")
        print("Swanson's Maintenance Tasks (SwM)")
        print("NFR Labeling")
        print("Software Evolution Tasks (SoftEvol)")
        classificationScheme = input("\nPlease enter classification scheme: ")

        # invalid classificationScheme control
        while (classificationScheme != "Swanson's Maintenance Tasks" and classificationScheme != "SwM" and classificationScheme != "NFR Labeling" and classificationScheme != "Software Evolution Tasks" and classificationScheme != "SoftEvol"):
            print("You entered invalid classificationScheme! ")
            classificationScheme = input("\nPlease enter classification scheme: ")

        if (classificationScheme == "Swanson's Maintenance Tasks" or classificationScheme == "SwM"):
            classificationScheme = "SwM tasks"  # I assign classificationScheme as SwM tasks as I used this string when I create the nested dictionary's values part (keysOfNames)

            # lists available classifications
            print("\nCorresponding features of SwM tasks are as follows: ")
            print("Adaptive Tasks")
            print("Corrective Tasks")
            print("Perfective Tasks")

            correspondingFeature = input("\nPlease enter the corresponding feature: ")

            # invalid correspondingFeature control
            while (correspondingFeature != "Adaptive Tasks" and correspondingFeature != "Corrective Tasks" and correspondingFeature != "Perfective Tasks"):
                print("You entered invalid correspondingFeature! ")
                correspondingFeature = input("\nPlease enter corresponding feature: ")

            # assign indexes to get values from dictionary using these indexes
            if (correspondingFeature == "Adaptive Tasks"):
                index = 0
            elif (correspondingFeature == "Corrective Tasks"):
                index = 1
            elif (correspondingFeature == "Perfective Tasks"):
                index = 2

            maxCommitValue = -1  # hold the value of the maximum commit value
            maxValueCommitter = ""  # hold the commiter name which commits max #of commits in a specific feature
            for key in IDsDict.keys():
                if(nestedDict[key][classificationScheme][index] > maxCommitValue):
                    maxCommitValue = nestedDict[key][classificationScheme][index]
                    maxValueCommitter = key

        elif (classificationScheme == "NFR Labeling"):
            # lists available classifications
            print("\nCorresponding features of NFR Labeling are as follows: ")
            print("Maintainability")
            print("Usability")
            print("Functionality")
            print("Reliability")
            print("Efficiency")
            print("Portability")

            correspondingFeature = input("\nPlease enter the corresponding feature: ")

            # invalid correspondingFeature control
            while (correspondingFeature != "Maintainability" and correspondingFeature != "Usability" and correspondingFeature != "Functionality" and correspondingFeature != "Reliability" and correspondingFeature != "Efficiency" and correspondingFeature != "Portability"):
                print("You entered invalid correspondingFeature! ")
                correspondingFeature = input("\nPlease enter corresponding feature: ")

            # assign indexes to get values from dictionary using these indexes
            if (correspondingFeature == "Maintainability"):
                index = 0
            elif (correspondingFeature == "Usability"):
                index = 1
            elif (correspondingFeature == "Functionality"):
                index = 2
            elif (correspondingFeature == "Reliability"):
                index = 3
            elif (correspondingFeature == "Efficiency"):
                index = 4
            elif (correspondingFeature == "Portability"):
                index = 5

            maxCommitValue = -1  # hold the value of the maximum commit value
            maxValueCommitter = ""  # hold the commiter name which commits max #of commits in a specific feature
            for key in IDsDict.keys():
                if (nestedDict[key][classificationScheme][index] > maxCommitValue):
                    maxCommitValue = nestedDict[key][classificationScheme][index]
                    maxValueCommitter = key

        elif (classificationScheme == "Software Evolution Tasks" or classificationScheme == "SoftEvol"):
            classificationScheme = "SoftEvol tasks"  # I assign classificationScheme as SoftEvol tasks as I used this string when I create the nested dictionary's values part (keysOfNames)
            # lists available classifications
            print("\nCorresponding features of NFR Labeling are as follows: ")
            print("Forward Engineering")
            print("Re-Engineering")
            print("Corrective Engineering")
            print("Management")

            correspondingFeature = input("\nPlease enter the corresponding feature: ")

            # invalid correspondingFeature control
            while (correspondingFeature != "Forward Engineering" and correspondingFeature != "Re-Engineering" and correspondingFeature != "Corrective Engineering" and correspondingFeature != "Management"):
                print("You entered invalid correspondingFeature! ")
                correspondingFeature = input("\nPlease enter corresponding feature: ")

            # assign indexes to get values from dictionary using these indexes
            if (correspondingFeature == "Forward Engineering"):
                index = 0
            elif (correspondingFeature == "Re-Engineering"):
                index = 1
            elif (correspondingFeature == "Corrective Engineering"):
                index = 2
            elif (correspondingFeature == "Management"):
                index = 3

            maxCommitValue = -1 #hold the value of the maximum commit value
            maxValueCommitter = "" #hold the commiter name which commits max #of commits in a specific feature
            for key in IDsDict.keys():
                if (nestedDict[key][classificationScheme][index] > maxCommitValue):
                    maxCommitValue = nestedDict[key][classificationScheme][index]
                    maxValueCommitter = key

        print("Committer named " + maxValueCommitter + " has maximum #of commits with " + correspondingFeature + " with a value of " + str(maxCommitValue))

    elif(option == 4):
      print("Exit!")
      exit(1)

    else:#this means user entered invalid input
        while (option < 1 or option > 4):  # loop if user enters an option that is out of range(1-4)
            print("Invalid Input!")
            option = int(input("Please enter an option between 1-4: "))






