import csv

scores = []
# with open("some_data.csv") as csvfile:
#     csvreader = csv.reader(csvfile)
#     # We can remove whitespace using lstrp and a map function to do it on one neat line
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

# Write a function that will return the mean to a new csv file

# Write a function that will read in the iris dataset
# def open_iris_csv(iris_csv):
#     with open(iris_csv) as opened_csv:
#         csv_reader = csv.reader(opened_csv)
#         for row in csv_reader:
#             print(row)
#
# print(open_iris_csv("iris.csv"))

# Write a function that will return the mean for each 'column'
# def column_iris_csv(iris_csv):
#     with open(iris_csv) as opened_csv:
#         # need to set it as a list
#         csv_reader = list(csv.reader(opened_csv))
#         # now we read from second row and after
#         csv_reader = csv_reader[1:]
#         mean_of_columns = []
#         # read in the first 4 rows of the csv
#         for i in range(4):
#             sum = 0
#             # now for each row in the csv reader
#             for row in csv_reader:
#                 print(i, row)
#                 sum += float(row[i])
#             mean = sum / (len(list(csv_reader)))
#             mean_of_columns.append(mean)
#         return mean_of_columns
#
# print(column_iris_csv("iris.csv"))