# 1. Variables & Data Types
name = "Addo Emmanuel"
age = 22
is_Student = True

print(name)
print(age)
print(is_Student)

# 2. Strings & f-strings
first = "Emmanuel"
last = "Addo"

full = (f"{first} {last}")
print(full)

# 3. Input & Output 
name = input("Addo Emmanuel:")
print(f"Welcome {name}")

# 4. Operators
x = 15
b = 4

print(x+b)
print(x-b)
print(x*b)
print(x/b)
print(x**b)

# 5. Conditional Statements
temperature = 35
if temperature > 30:
    print("Hot")
elif temperature > 20:
    print("Warm")
else:
    print("Cold")       

# 6. Loops
for i in range(10):
    print(i)

# While loop  
count = 0

while count < 5:
    print(count)
    count += 1  

# 7. Lists
numbers = [1, 2, 3, 4, 5]
print(numbers[0])
numbers.append(6)
numbers.pop()

for num in numbers:
    print(num)

# 8. Dictionaries
person = {
    "name": "Emmanuel",
    "age": 22,
    "country": "Ghana"
}
print(person["name"])
person["age"] = 23
print(person["age"])

# 9. Functions
def greet(name):
    print(f"Hello {name}")

# 10. Tuple 
colors = ("red", "green", "blue")
print(colors[0])   


# Challenge Recap
# Ask user for name
# Store it in a list
# Use a function to greet them

# create an empty list
names = []

# ask user for name
name = input("Enter your name: ")

# store it in the list
names.append(name)

# create a function
def greet(name):
    print(f"Hello {name}")

# use the function
for n in names:
    greet(n)