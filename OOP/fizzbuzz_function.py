
# We want to create a function for Fizzbuzz
# There will be multiple parameters for the function
# The function will take all these parameters and set them as the arguments for each part of the program.

def fb_function(counter_value_input, limit_input, increment_input, fizz_input, buzz_input, first_val_input, second_val_input):

    # # NULL values
    # counter_value = ''
    # limit = ''
    # counter = ''
    #
    # # Fizz Buzz inputs
    # fizz_input = ''
    # buzz_input = ''
    #
    # # First and second values to divide the counter by
    # first_val = ''
    # second_val = ''

    # # Starting counter value
    # while not counter_value.isnumeric():
    #     counter_value = counter_value_input
    #     counter = int(counter_value)
    #     if not counter_value.isnumeric():
    #         print("That's not a number, try again")
    #
    # # Limit value
    # while not limit_input.isnumeric():
    #     limit = limit_input
    #     if not limit.isnumeric():
    #         print("That's not a number, try again")
    #
    # # First and second value
    #
    # while not first_val.isnumeric():
    #     first_val = first_val_input
    #     if not first_val.isnumeric():
    #         print("That's not a number, try again")
    #
    # while not second_val.isnumeric():
    #     second_val = second_val_input
    #     if not second_val_input.isnumeric():
    #         print("That's not a number, try again")

    # Print each number in turn

    while counter_value_input < limit_input:
        if counter_value_input % int(first_val_input) == 0 and counter_value_input % int(second_val_input) == 0:
            print(fizz_input + ' ' + buzz_input)
        elif counter_value_input % int(first_val_input) == 0:
            print(fizz_input)
        elif counter_value_input % int(second_val_input) == 0:
            print(buzz_input)
        elif counter_value_input == limit_input:
            break
        else:
            print(counter_value_input)
        counter_value_input += increment_input
        if counter_value_input + increment_input > limit_input:
            counter_value_input = limit_input


# def fb_function(counter_value_input, limit_input, increment_input, fizz_input, buzz_input, first_val_input, second_val_input):
print(fb_function(1, 100, 2, "fizz", "buzz", 3, 5))

