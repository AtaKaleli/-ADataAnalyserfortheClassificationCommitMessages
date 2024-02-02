import re

a = {
    "borsh":{
        "swm":[0,0,0],
        "nfr":[0,0,0,0,0,0],
        "soft":[0,0,0,0]
    },
    "luca":{
        "swm":[0,0,0],
        "nfr":[0,0,0,0,0,0],
        "soft":[0,0,0,0]
    }
}

query = ['0','1','0','0','1','1','0','0','0','0','0','1','0','2']
query = "".join(query)
pattern = re.match("(\d{3})(\d{6})(\d{4})(\d+)",query).groups()
# for pat in pattern: shows pattern groups
#     print(pat)
#pattern[0] = "010" --> pattern[0][1] = "1"    (convertable to integer using int())
#pattern[1] = "001000"
#pattern[2] = "0010"
#pattern[3] = "2" -> ID of the commiter

#idea:classıfıcatıon degerlerını dırekt toplayabılırız, 0 lar zaten etkı etmeyecek
key = "luca"
a[key]["swm"][0] = 1
a[key]["swm"][1] = 2
a[key]["nfr"][4] = 3
a[key]["soft"][2] = 4
a["borsh"]["swm"][1] = 5
a["borsh"]["soft"][2] = 6
# for i in range(3): #for swm
#     a[key]["swm"][i] += int(pattern[0][i])
# for i in range(6): #for nfr
#     a[key]["nfr"][i] += int(pattern[1][i])
# for i in range(4): #for soft
#     a[key]["soft"][i] += int(pattern[2][i])


for key,value in a.items():
    print(key,"-",value)



# key = "borsh"
# for query in queries:
#     query = "".join(query)
#     pattern = re.match("(\d{3})(\d{6})(\d{4})", query).groups()
#
#     for i in range(3):  # for swm
#         a[key]["swm"][i] += int(pattern[0][i])
#     for i in range(6):  # for nfr
#         a[key]["nfr"][i] += int(pattern[1][i])
#     for i in range(4):  # for soft
#         a[key]["soft"][i] += int(pattern[2][i])
# print(a[key])
