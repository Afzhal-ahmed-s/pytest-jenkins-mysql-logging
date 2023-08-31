data = ["Java", 2021, True, False]
data2 = ["Por thozil", "Maamannan"]
# print(data)
# print(len(data))
#
# print(data[1])
# print(data[1:3])
# print(data[1:])
# print(data[:2])
#
# for i in data:
#     print(i)
#
# for i in range(0, len(data)-1):
#     print(data[i])

finalList = data + data2 # concatenate list
print(finalList)

finalList.insert(0, "Java script") #inserts the element at that index and pushes the next coming elements one place to the right or one index more
print(finalList)

finalList.remove("Por thozil")
finalList.remove(finalList[0])
print(finalList)

