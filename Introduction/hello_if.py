# CONTROL FLOW

# age = int(input("How old are you? \n"))
#
# if age >= 18:
#     print("You can see ")
# elif age == 18:
#     print("you are only just old enough")
# else:
#     print("you are not old enough")

# U, PG, 12A, 15, 18

movie = input("What type of movie do you want to see? (u, pg, 12, 12a, 15, 18) \n")

if movie.lower() == "u":
    print("All ages can see this movie")
elif movie.lower() == "pg":
    print("you need parental guidance when seeing this movie")
elif movie.lower() == "12a" or movie.lower() == "12":
    print("you need to be 12 or above and accompanied by an adult")
elif movie.lower() == "15":
    print("you need to be 15 years old or above to see this movie")
elif movie.lower() == "18":
    print("you need to be 18 years old or above to see this movie")
else:
    print("enter a valid film rating")