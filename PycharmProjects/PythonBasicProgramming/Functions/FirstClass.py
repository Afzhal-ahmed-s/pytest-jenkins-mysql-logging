class A:

    def __init__(self):
        print("This is constructor of class A.")

    def welcome(self):
        print("This is a class function.")

    def sum(self, a, b):
        print("Sum is: "+ str(a+b))

    def multiply(self, a, b):
        return a*b

obj = A();
obj.welcome()
obj.sum(5,6)
print(obj.multiply(3,8))