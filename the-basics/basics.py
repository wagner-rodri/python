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