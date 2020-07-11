# FIZZBUZZ
# start at 1
counter = int(input("Where do you want to start from: \n"))
limit = int(input("Please input your limit: \n"))


# print each number in turn
while counter < limit:
    if counter % 3 == 0 and counter % 5 == 0:
        print("FizzBuzz")
    elif counter % 3 == 0:
        print("Fizz")
    elif counter % 5 == 0:
        print("Buzz")
    elif counter == limit:
        break
    else:
        print(counter)
    counter += 1

# change where it is fizz, buzz and fizzbuzz
# make it an interactive game, change the numbers, fizz, buzz and fizzbuzz to something else


# accept user input for custom fizz buzz? done
# change the number we increment by? done
# change the values of fizz and buzz?

