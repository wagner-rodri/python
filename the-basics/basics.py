import datetime
myNow = datetime.datetime.now()
print(myNow)

myNumber = 28
myText = 'Hello'

print(myNumber, myText)

x = 10
y = '18' 
z = 10.1

sum1 = x + x
sum2 = y + y

print(sum1, sum2)
print(type(x), type(y), type(z))

monday_temperatures = [9.1, 8.8, 7.5]
student_grades = {'Marry': 9.1, 'Sim': 8.8, 'John': 7.5}

mySum = sum(student_grades.values())
length = len(student_grades)
mean = mySum / length
print(mean)

monday_temperatures = (1, 4, 5)
sunday_temperatures = [1, 4, 5]
sunday_temperatures.append(8.5)
sunday_temperatures.remove(4)
sunday_temperatures[1:]
sunday_temperatures[-3:-1]


student_grades = {'Marry': 9.1, 'Sim': 9.8, 'John': 7.5}

def mean(value):
    if type(value) == dict:
        theMean = sum(value.values()) / len(value)
    else:
        theMean = sum(value) / len(value)

    return theMean

print(mean(student_grades))

# def foo(temperature):
#     if temperature > 25:
#         return "Hot"
#     elif temperature >= 15 and temperature <= 25:
#         return "Warm"
#     else:
#         return "Cold"

# userInput = input("Enter temperature: ")

# print(foo(int(userInput)))

name = input("Enter your name: ")
surname = input("Enter your surname: ")
message3 = 'Hello, %s %s!' % (name, surname)
message4 = f'Hello, {name} {surname}!'
print(message3)
print(message4)