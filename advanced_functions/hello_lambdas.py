# Lambda is a way of doing anonymous functions

# Without having to define the function in advance
# Alas doing it on the fly

# def add(n1, n2):
#     return n1+n2
#
# print(add(2, 2))
#
# add_lambda = lambda n1, n2: n1 + n2
#
# print(add_lambda(2, 2))
#
# # You wont use lambdas like this all the time
# # You will use them with maps and filters
#
# numbers = [192, 402, 5, 94, 241, 23, 74]

# Previously with map, we needed a function defined prior but now, we can use lambda
# result = map(lambda x: x * x + 3, numbers)
# print(list(result))

savings = [234.00, 21.00, 52.23, 1.23]

# in a new list called bonus
# the result of savings  with 10% added

# bonus = list(map(lambda x: x + 0.1*x, savings))
# print(bonus)

# in a new list called even savings
# keep only saving amounts that are even
# use filter

even_savings = list(filter(lambda x: x % 2 == 0, savings))
print(even_savings)