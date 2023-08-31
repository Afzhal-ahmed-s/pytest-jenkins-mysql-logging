#StringOperation_4

data = "  Afzhal Ahmed S  "

print(data.replace("Afzhal", "Niyas"))
print(data.replace("zh", "ZH"))
print(data.replace("Af","$$$").replace("hm", "###")) #replace chaining

print(data.find("Afzhal")) #returns staring index of the word or character
print(data.find("Mayiru"))

data2 = "Kavundampalayam Kovai Pudur Pothanur"

splited = data2.split(" ")
print(len(splited))

for i in splited:
    print(i)

str1 = "  Afzhal"
str2 = "afZhal  "

if(str1.strip() == str2.strip()):
    print("insenstivity Matches")
else:
    print("insenstivity does not matches")

if(str1.strip().upper() == str2.strip().upper()):
    print("chaining reaction succeeds.")
else:
    print("chaining reaction doesn't succeeds.")