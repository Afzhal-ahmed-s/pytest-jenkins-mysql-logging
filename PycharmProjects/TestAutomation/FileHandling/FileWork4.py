obj = open("/home/afzhal-ahmed-s/PycharmProjects/py1.txt",'r')
print(obj.tell())
obj.readline()
print(obj.tell())
obj.readline()
obj.seek(5)
print(obj.tell())

