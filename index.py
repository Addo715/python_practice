# variables and data types
name = "Emmanuel"   # string
age = 20            # integer
height = 5.9        # float
is_student = True   # boolean

# Stings & f-strings
first = "Emmanuel"
last = "Addo"

full = f"{first} {last}"
print(full)

print(len(full))       # length
print(full.upper())    # uppercase

# Input and Output
name = input("Enter your name: ")
print(f"Hello {name}")

# Operators
a = 10
b = 3

print(a + b)   # add
print(a - b)   # subtract
print(a * b)   # multiply
print(a / b)   # divide
print(a % b)   # remainder

# If Statements
temperature = 35

if temperature > 30:
    print("Hot day")
elif temperature > 20:
    print("Nice day")
else:
    print("Cold day")


# loops
for i in range(5):
    print(i)

# While loop
count = 0

while count < 5:
    print(count)
    count += 1

# Lists (Arrays)
numbers = [1, 2, 3, 4, 5]

print(numbers[0])     # first item
numbers.append(6)     # add item
numbers.pop()         # remove last

for num in numbers:
    print(num)

# Dictionaries(objects)
person = {
    "name": "Emmanuel",
    "age": 20
}

print(person["name"])
person["age"] = 21

# Functions

def greet(name):
    print(f"Hi {name}")


greet("Emmanuel")

# Function with return value


def add(a, b):
    return a + b


result = add(5, 3)
print(result)        # 8

# Function with default value


def greet(name="stranger"):
    print("Hello,", name)


greet()              # Hello, stranger
greet("Alice")

# Files
# write file
with open("file.txt", "w") as file:
    file.write("Hello")

# read file
with open("file.txt", "r") as file:
    print(file.read())

# Error Handling
try:
    x = int(input("Enter number: "))
    print(x)
except:
    print("Invalid input")

# Classes (Basic OOP)


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi {self.name}")


p = Person("Emmanuel")
p.greet()

# Tuples & Sets
# Tuple — like a list but CANNOT be changed
colors = ("red", "green", "blue")
print(colors[0])        # red

# Set — unique values only, no duplicates
unique = {1, 2, 3, 2, 1}
print(unique)           # {1, 2, 3}
