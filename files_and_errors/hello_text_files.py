# r - Read mode (default)
# w - write mode (if no file, creates one; if file, truncate)
# x - create mode (if file, fails)
# a - append mode (if no file, create one; if file, appends
# t - text mode
# b - binary mode
# + - reading and writing

# def open_and_print_file(filename):
#     try:
#         opened_file = open(filename, "r")
#         file_line_list = opened_file.readlines()
#
#         for line in file_line_list:
#             print(line.rstrip('\n'))
#
#         opened_file.close()
#
#     except FileNotFoundError:
#         print("File cannot be found, please check filename provided")
#         raise
#
# file = open("order.txt")
# print(file.readline())
# print(file.readline())
# print(file.readline())
# # It will read a new line and the original line is lost from the buffer
#
# # New text lines come with a new line indicator which is why it produces
# # Big gaps when running the function

# def open_and_print_file(filename):
#     try:
#         with open(filename, 'r') as opened_file:
#             file_line_list = opened_file.readlines()
#
#             for line in file_line_list:
#                 print(line.rstrip('\n'))
#
#     except FileNotFoundError:
#         print("File cannot be found, please check filename provided")
#         raise
#
# open_and_print_file("order.txt")

# with open("order.txt", "w") as opened_file:
#     opened_file.write("Cheeseburger")
#


def append_to_file(filename, order):
    try:
        with open(filename, "a") as opened_file:
            opened_file.write(order + '\n')

    except TypeError:
        print("Order needs to be a string. Please try again.")


append_to_file("order.txt", "pasta")
append_to_file("order.txt", "hotdog")
append_to_file("order.txt", "kebab")
append_to_file("new_order.txt", "pizza")