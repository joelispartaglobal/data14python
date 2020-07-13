# FIZZBUZZ

# Starting counter value
counter = int(input("What do you want your starting counter value to be? \n"))

# Counter text
counter_text = input("What do you want the counter text to be? \n")

# Limit value
limit = int(input("What do you want your limit value to be? \n"))

# Fizz Buzz inputs
fizz = input("What do you want 'Fizz' to be? \n")
buzz = input("What do you want 'Buzz' to be? \n")

# First and second values to divide the counter by
first_val = ''
second_val = ''

while not first_val.isnumeric():
    first_val = input("What do you want your first divisive value to be? \n")
    if not first_val.isnumeric():
        print("That's not a number, try again")

while not second_val.isnumeric():
    second_val = input("What do you want your second divisive value to be? \n")
    if not second_val.isnumeric():
        print("That's not a number, try again")

# Print each number in turn

while counter < limit:
    if int(counter) % int(first_val) == 0 and int(counter) % int(second_val) == 0:
        print(fizz + ' ' + buzz)
    elif int(counter) % int(first_val) == 0:
        print(fizz)
    elif int(counter) % int(second_val) == 0:
        print(buzz)
    elif int(counter) == limit:
        break
    else:
        print(counter_text)
    counter += 1


# change where it is fizz, buzz and fizzbuzz done
# make it an interactive game, change the numbers, fizz, buzz and fizzbuzz to something else done


# accept user input for custom fizz buzz? done
# change the number we increment by? done
# change the values of fizz and buzz?

