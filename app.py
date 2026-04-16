students_count = 1000
print(students_count)

# boolean
is_published = True

# string
course = "Python"
print(len(course))
print(course[-1])
print(course[0:3])

new = "Python \"Code"
print(new)


first = "Emmanuel"
last = "Addo"
# full = first + " " + last
full = f"{first} {last}"
print(full)

program = "Python for Beginners"
print(program.upper())
print(program.lower())
print(program.title())


# numbers 
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

# working with numbers
import math
print(round(2.9))
print(abs(-2.9))

# conditional statements
temperature = 35
if temperature > 30:
    print("It's a hot day")


def greet(name):
    print(f"Hi {name}")