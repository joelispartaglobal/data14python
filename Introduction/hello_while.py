# counter = 0
#
# while counter < 10:
#     print(f"still counting! {counter}")
#     if counter == 6:
#         break
#     counter += 1
#
# print("we've escaped the while loop")

# for number in range(10):
#     print(number)

age_input = ""

while not age_input.isnumeric():
    age_input = input("Enter your age:\n")
    if not age_input.isnumeric():
        print("That's not a number, try again")


age = int(age_input)


# print("You are" + ' ' + str(age))