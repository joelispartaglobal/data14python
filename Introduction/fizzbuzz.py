# FIZZBUZZ
# start at 1
counter = ''
limit = ''


while not counter.isnumeric():
    counter = input("What do you want your counter value to be? \n")
    if not counter.isnumeric():
        print("That's not a number, try again")

counter_text = input("What do you want the counter text to be? \n")

while not limit.isnumeric():
    limit = input("What do you want your limit value to be? \n")
    if not limit.isnumeric():
        print("That's not a number, try again")


fizz = input("What do you want 'Fizz' to be? \n")
buzz = input("What do you want 'Buzz' to be? \n")

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

# print each number in turn

while int(counter) < int(limit):
    if int(counter) % int(first_val) == 0 and counter % int(second_val) == 0:
        print(fizz + ' ' + buzz)
    elif int(counter) % int(first_val) == 0:
        print(fizz)
    elif int(counter) % int(second_val) == 0:
        print(buzz)
    elif int(counter) == int(limit):
        break
    else:
        print(counter_text)
    counter += 1


# change where it is fizz, buzz and fizzbuzz done
# make it an interactive game, change the numbers, fizz, buzz and fizzbuzz to something else done


# accept user input for custom fizz buzz? done
# change the number we increment by? done
# change the values of fizz and buzz?

