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

# end at 100

# if divisible by 3, instead of a number, "fizz"
# if divisible by 5, instead of a number, "buzz"
# if divisible by 3 and 5, instead of a number, "fizzbuzz"

# accept user input for number to count up to
# accept user input for number to start from

# accept user input for custom fizz buzz?
# change the number we increment by?
# change the values of fizz and buzz?

