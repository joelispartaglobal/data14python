import csv

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

# Write a function that will return the mean to a new csv file

def new_iris_csv(new_iris_csv):
    with open(new_iris_csv, "w", newline="\n") as opened_csv:
        data_to_write = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
        csv_writer = csv.writer(opened_csv)
        with open("iris.csv") as iris_csv:
            # need to set it as a list
            csv_reader = list(csv.reader(iris_csv))
            # now we read from second row and after
            csv_reader = csv_reader[1:]
            mean_of_columns = []
            # read in the first 4 rows of the csv
            for i in range(4):
                sum = 0
                # now for each row in the csv reader
                for row in csv_reader:
                    print(i, row)
                    sum += float(row[i])
                mean = sum / (len(list(csv_reader)))
                mean_of_columns.append(mean)
            mean_of_columns_2 = mean_of_columns
        csv_writer.writerow([f] for f in data_to_write)
        csv_writer.writerow([g] for g in mean_of_columns_2)


new_iris_csv("new_iris.csv")
