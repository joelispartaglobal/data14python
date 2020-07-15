students = ["DAVID", "Lee", "RICHARD"]

result = filter(str.isupper, students)
# Returns anything that is true i.e. the first parameter
# And removes anything that is false

print(list(result))

# Write a function that returns true if even and divisible by 3

def division(a):
    return a % 2 == 0 and a % 3 == 0

numbers = list(range(100))

print(list(filter(division, numbers)))
