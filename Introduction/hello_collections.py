# # lists (aka arrays)
#
# shopping_list = ["eggs", "sausages", "cheese", "bread"]
#
# print(shopping_list)
# # print(type(shopping_list))
#
# # lists can be anything
# #
# # print(shopping_list[0])
# # print(shopping_list[0:3])
# # print(shopping_list[-1])
# # print(len(shopping_list))
#
# shopping_list.append("mushrooms")
# print(shopping_list)
#
# shopping_list.append("coffee")
# print(shopping_list)
#
# shopping_list.remove("cheese")
# print(shopping_list)
#
# shopping_list.append("eggs")
# print(shopping_list)
#
# shopping_list.pop()
# print(shopping_list)
#
# pop_return = shopping_list.pop()
# print(pop_return)

# # Tuples
#
# colours = ("blue", "purple", "turquoise")
# print(colours)
# print(type(colours))
# print(colours[-1])
#
# # TUPLES ARE IMMUTABLE - CANNOT BE CHANGED
#
# print(colours.count("orange"))
# print(colours.index("purple"))
#

# DICTIONARIES

# my_dict = {"key": "Value"}
# print(my_dict)
# print(type(my_dict))
#
# bigger_dictionary = {
#     "key1": "value1",
#     "key2": "value2",
#     "key3": "value3"
# }

# my_dictionary = {
#     "name": "Joe",
#     "age": 24,
#     "birthday": "03/10/95",
#     "Favourite colour": "blue",
#     "favourite animal": "raccoon",
#     "favourite music": "house"
# }
#
# print(my_dictionary)
#
# print(my_dictionary["name"])
# # dict[key]
#
# my_dictionary["favourite music"] = "Trance"
# my_dictionary["new_key"] = "Some new value"
#
# print(my_dictionary)
#
# del my_dictionary["new_key"]
#
# print(my_dictionary)
# print(my_dictionary.keys())
# print(my_dictionary.values())

data14_dictionary = {
    "trainer": "David Harvey",
    "location": "Birmingham",
    "course": "data engineering",
    "duration": "12 weeks",
    "topics": ["business skills", "sql", "critical thinking", "agile", "python", "big data", "nosql", "cloud", "project"],
    "schedule": {
        "week 1": "Business week",
        "week 2": "SQL"
    },
    "number of participants": "11"

}

print(data14_dictionary)

print(data14_dictionary["topics"][4])