# import datetime
# myNow = datetime.datetime.now()
# print(myNow)

# myNumber = 28
# myText = 'Hello'

# print(myNumber, myText)

# x = 10
# y = '18' 
# z = 10.1

# sum1 = x + x
# sum2 = y + y

# print(sum1, sum2)
# print(type(x), type(y), type(z))

# monday_temperatures = [9.1, 8.8, 7.5]
# student_grades = {'Marry': 9.1, 'Sim': 8.8, 'John': 7.5}

# mySum = sum(student_grades.values())
# length = len(student_grades)
# mean = mySum / length
# print(mean)

# monday_temperatures = (1, 4, 5)
# sunday_temperatures = [1, 4, 5]
# sunday_temperatures.append(8.5)
# sunday_temperatures.remove(4)
# sunday_temperatures[1:]
# sunday_temperatures[-3:-1]


# student_grades = {'Marry': 9.1, 'Sim': 9.8, 'John': 7.5}

# def mean(value):
#     if type(value) == dict:
#         theMean = sum(value.values()) / len(value)
#     else:
#         theMean = sum(value) / len(value)

#     return theMean

# print(mean(student_grades))

# def foo(temperature):
#     if temperature > 25:
#         return "Hot"
#     elif temperature >= 15 and temperature <= 25:
#         return "Warm"
#     else:
#         return "Cold"

# userInput = input("Enter temperature: ")

# print(foo(int(userInput)))

# name = input("Enter your name: ")
# surname = input("Enter your surname: ")
# message3 = 'Hello, %s %s!' % (name, surname)
# message4 = f'Hello, {name} {surname}!'
# print(message3)
# print(message4)


# for loops

# monday_temperatures = [9.1, 8.8, 7.5]

# for temperature in monday_temperatures:
#     print(round(temperature))

# for letter in 'Hello!':
#     print(letter)

# for loops in dict

# student_grades = {'Marry': 9.1, 'Sim': 9.8, 'John': 7.5}

# for grades in student_grades.keys():
#     print(grades)

# 

# while True:
#     username = input('Enter username: ')
#     if username == 'pypy':
#         break
#     else:
#         continue

# list comprehension

# temps = [221, 234, 340, -170, 230]

# newTemps = [temp / 10 for temp in temps]

# print(newTemps)

# list comprehension with if

# temps = [221, 234, 340, -999, 230]

# newTemps = [temp / 10 for temp in temps if temp != -999]

# print(newTemps)

# print(type(3))

# list comprehension with if-else

# temps = [221, 234, 340, -999, 0, 230]

# newTemps = [temp / 10  if temp != -999 else 0 for temp in temps]

# print(newTemps)

# a = ['1.2', '2.6', '3.3']

# def convertList(array):
#     convertedList = []
#     for value in array:
#         cNumber = float(value)
#         convertedList.append(cNumber)
#     return convertedList

# def sumValues(array):
#     soma = sum(convertList(array))
#     return soma

# print(sumValues(a))

# multiples args in function

# def mean(*args):
#    return args

# multiples args in function with key word args

# def mean(**kwargs):
#    return args

# myFile = open("fruits.txt")
# content = myFile.read()
# myFile.close()

# with open("files/fruits.txt") as myFile:
#     content = myFile.read()

# print(content)

# with open("files/vegetables.txt", "w") as myFile:
#     myFile.write("Tomato")

# import time

# while True:
#     with open("files/fruits.txt") as file:
#         print(file.read())
#         time.sleep(1)
