import csv

# scores = []
# with open("some_data.csv") as csvfile:
#     csvreader = csv.reader(csvfile)
#     # We can remove whitespace using lstrip and a map function to do it on one neat line
#     headers = list(map(str.lstrip, next(csvreader)))
#     # Next moves us one along the iterable
#     for row in csvreader:
#         scores.append(int(row[-1]))
#
# print(headers)
# print(scores)
# scores stored as strings
# get rid of the header
#
# with open("some_data.csv") as csvfile:
#     csvreader = csv.reader(csvfile)
#     print(list(csvreader)) # List of lists
# data_to_write = [["David", 5], ["Paula", 6], ["Nish", 7]]
#
# with open("new_data.csv", "w", newline="\n") as csvfile:
#     csv_writer = csv.writer(csvfile)
#     # for row in data_to_write:
#     #     csv_writer.writerow(row)
#     csv_writer.writerows(data_to_write)
#

