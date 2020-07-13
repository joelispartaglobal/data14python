
# We want to create a function for Fizzbuzz
# There will be multiple parameters for the function
# The function will take all these parameters and set them as the arguments for each part of the program.


# NULL values
counter_value = ''
limit = ''
counter = ''

# Starting counter value
while counter_value.isnumeric():
    counter_value = input("What do you want your starting counter value to be? \n")
    counter = int(counter_value)
    if not counter_value.isnumeric():
        print("That's not a number, try again")


# Limit value
while limit.isnumeric():
    limit = input("What do you want your limit value to be? \n")
    if not limit.isnumeric():
        print("That's not a number, try again")

# Fizz Buzz inputs
fizz = input("What do you want 'Fizz' to be? \n")
buzz = input("What do you want 'Buzz' to be? \n")

# First and second values to divide the counter by
first_val = ''
second_val = ''

while first_val.isnumeric():
    first_val = input("What do you want your first divisive value to be? \n")
    if not first_val.isnumeric():
        print("That's not a number, try again")

while second_val.isnumeric():
    second_val = input("What do you want your second divisive value to be? \n")
    if not second_val.isnumeric():
        print("That's not a number, try again")

# Print each number in turn

while counter < int(limit):
    if counter % int(first_val) == 0 and counter % int(second_val) == 0:
        print(fizz + ' ' + buzz)
    elif counter % int(first_val) == 0:
        print(fizz)
    elif counter % int(second_val) == 0:
        print(buzz)
    elif counter == limit:
        break
    else:
        print(counter)
    counter += 1




