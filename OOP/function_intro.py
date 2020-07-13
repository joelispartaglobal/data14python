# # Don't
# # Repeat
# # Yourself
#
# # We can define a function and specify the functionality, whenever we want to use that code we can call the function
#
# def print_something():
#     print("something")
#
# print_something()
#
# def print_something_multiple(some_string, number_of_times):
#     string_to_print = some_string * number_of_times
#     print(string_to_print)
#
# print_something_multiple("Woohoo!", 5)

# def repeat_string(string_to_repeat, number_of_repeats):
#     string_to_return = string_to_repeat * number_of_repeats
#     return string_to_return
#
#
# my_string = repeat_string("hello", 5)
# print(my_string)

# Write a function for addition

# def addition(a, b):
#     return a + b
#
# print(addition(1, 2))

# we can set the number of repeats within the parameter

# def repeat_string(string_to_repeat, number_of_repeats=3):
#     string_to_return = string_to_repeat * number_of_repeats
#     return string_to_return
#
#
# my_string = repeat_string("hello")
# print(my_string)

# def product_list(*multiargs):
#     for num in multiargs:
#         print(num)


# def find_product(*multiargs):
#     # Return the product (all numbers multiplied together)
#     if len(multiargs) < 1:
#         return None
#     else:
#         product = 1
#         for num in multiargs:
#             product *= num
#         return product
#
#
# print(find_product(1, 2, 3, 4, 5))

# We can give Python hints on what the type will be
def repeat_string(string_to_repeat: str, number_of_repeats: int = 3) -> str:
    string_to_return = string_to_repeat * number_of_repeats
    return string_to_return


print(repeat_string("Woohoo!", 4))