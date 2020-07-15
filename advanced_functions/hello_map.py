data14 = ["Katie", "Juxhen", "Joe"]

# # as a list, the same names but in upper case
#
# data14upper = [x.upper() for x in data14]
# print(data14upper)

# Map applies a function to an iterable

# data14upper = map(str.upper, data14)
# print(list(data14upper))

# We can iterate it or we can force it to be in a list
# for name in data14upper:
#     print(name)

# Write a function that squares a number and adds 3

# If one list is longer than the other list, it will stop at the shortest list
numbers = [1, 2, 3, 4, 5]
adds = [10, 100, 1000]

def square(num, add):
    number = num * num + add
    return number

num_map = map(square, numbers, adds)

print(list(num_map))
