# Hello World
print("Hello, World!")

# Variables
name = "John"
print(name)

name = "Jane"
print(name)

# Manipulation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

x = 10
y = 5
sum = x + y
difference = x - y
product = x * y
quotient = x / y
remainder = x % y
print(sum, difference, product, quotient, remainder)

# Dictionaries
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person["name"])
print(person.get("age"))
person["age"] = 35
person["occupation"] = "Engineer"
for key, value in person.items():
    print(key, value)

# Lists
fruits = ["apple", "banana", "orange"]
print(fruits[0])
print(fruits[1:3])
fruits.append("grape")
fruits.insert(1, "kiwi")
fruits.remove("banana")
del fruits[0]
for fruit in fruits:
    print(fruit)

# Calculations
x = 10
y = 5
sum = x + y
difference = x - y
product = x * y
quotient = x / y
remainder = x % y
print(sum, difference, product, quotient, remainder)

# Classes and OOP
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

person = Person("John", 30)
print(person.name)
print(person.age)
person.greet()

# Data Structures
numbers = [1, 2, 3, 4, 5]
print(len(numbers))

fruits = {"apple", "banana", "orange"}
fruits.add("grape")
print(fruits)

my_tuple = (1, 2, 3)
print(my_tuple)
print(my_tuple[0])

# Loops
for i in range(1, 6):
    print(i)

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

counter = 0
while counter < 5:
    print(counter)
    counter += 1

# Error Handling
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero")
except Exception as e:
    print("Error:", str(e))
