from configparser import ConfigParser

config = ConfigParser()

config.read("../Configuration/Config.cfg")

print(config.get("Section1", "username"))

try:
    # obj = open("summa/dummy")
    userInput1 = input("Enter first number: ")
    userInput2 = input("Enter second number: ")

    c = int(userInput1) + int(userInput2)
    print(c)

except:
    print("Into excpet block, please give correct input.")

finally:
    print("Always execute this line in 'finally' block.")