# =========================
# LOOPS
# =========================
for i in range(4):
    print("aniqa")
for char in "aniqamukhtar":
    print(char)

count = 1
while count <=5:
    print(count)
    count += 1
for i in range(3):
    print("outer loop")
    for j in range(3):
        print("    inner loop")
#muliplication table 
number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
#append function 
i=4
rows=i
cols=i
matrix=[]
for r in range(rows):
     rows=[]
for c in range(cols):
    rows.append(0)
    matrix.append(rows)
for rows in matrix:
    print(' '.join(map(str,rows)))
#charaters count 
count1=0
for char in "banana":
    if char== "a":
        count1 += 1
print(count1)

st= "python"
rev=" "
for ch in st:
    rev= ch + rev
print (rev)
student = {"name": "ali","age" :21 ,"grade" : "A"}
for key in student:
    print(key)
    print(student[key])
#Find the largest number without max()
numbers = [12, 45, 7, 89, 23, 56]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print("Largest:", largest)
# =========================
# functions , lamda , modules
# =========================
def greet():
    print("hellow aniqa")
greet()

def greet(name):
    print("hellow", name )
    print(greet)
greet ("ali")
greet("sara")
def add(a,b):
    return(a+b)
result=add (3,4)
print(result)
#-----Function to check prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
print(is_prime(17))
print(is_prime(20))
#Function using *args
def calculate_sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(calculate_sum(10, 20))
print(calculate_sum(10, 20, 30, 40))
#Function using **kwargs
def student(**info):
    for key, value in info.items():
        print(key, ":", value)
student(name="Aniqa", age=21, course="AI", semester=5)
#-------variables inside funtion =local
#variables outside funtions = global
#lamda function small one line code for small functions 
# syntax lambda parameters: expression-------
square = lambda x: x * x
print(square(5))

multiply = lambda a, b: a * b
print(multiply(4, 6))

numbers = [20, 65, 45, 90, 30, 75]
result = list(filter(lambda x: x > 50, numbers))
print(result)

names = ["ali", "sara", "ahmed", "aniqa"]  #uppercase
result = list(map(lambda name: name.upper(), names))
print(result)

info = lambda name, age: f"{name} is {age} years old"
print(info("Ali", 20))
number = [1, 2, 3, 4]
square = list(map(lambda x: x * x, number))
print(square)
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)
#Sort using lambda
students = [
    ("Ali", 75),
    ("Sara", 90),
    ("Ahmed", 65),
    ("Aniqa", 85)
]
students.sort(key=lambda x: x[1])
print(students)
#-----module to store long code import r skty hain ------
import math     #full library import
print(math.sqrt(144))
from math import sqrt     #import single function
print(sqrt(25))

from math import factorial
print(factorial(5))

import calculator
print(calculator.add(10, 5))
print(calculator.multiply(10, 5))



