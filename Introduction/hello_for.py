# FOR LOOPS

# shopping_list = ["eggs", "bacon", "bread"]
# favourite_colours = ["yellow", "purple", "turquoise"]
#
# for item in shopping_list:
#     for colour in favourite_colours:
#         print(colour, item)

# dict_data = {
#     1: {"name": "Joe", "animal": "raccoon"},
#     2: {"name": "Alex", "animal": "all dogs"},
#     3: {"name": "Ben", "animal": "flamingo"},
#     4: {"name": "Evie", "animal": "gorilla"},
#     5: {"name": "Charlotte", "animal": "giraffe"}
#
# }

# for key in dict_data:
#     for inner_key in dict_data[key]:
#         print(dict_data[key][inner_key])

# for key in dict_data:
#     print(dict_data[key]["name"])

# for key in dict_data:
#     print(f"{dict_data[key]['name']}'s favourite animal is {dict_data[key]['animal']}")

# chinese_menu

chinese_menu = {
    1: {'dish': 'egg fried rice', 'price': "1.60"},
    2: {'dish': 'egg and sweetcorn soup', 'price': "2.40"},
    3: {'dish': 'sweet and sour chicken', 'price': "3.50"},
    4: {'dish': 'prawn crackers', 'price': "1.00"}

}

for key in chinese_menu:
    print(f"{chinese_menu[key]['dish']} costs £{chinese_menu[key]['price']}")