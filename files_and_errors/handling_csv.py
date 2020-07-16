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