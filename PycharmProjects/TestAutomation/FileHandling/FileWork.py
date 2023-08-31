obj = open("/home/afzhal-ahmed-s/PycharmProjects/py.txt", 'r')

# print(obj.read())

# #read one line
# print(obj.readline())
# print(obj.readline())

# #read few characters in a line
# print(obj.read(10))

# #printing character by character
# for i in obj.read():
#     print(i)

s = obj.readline()

while(s):
    print(s)
    s = obj.readline()
