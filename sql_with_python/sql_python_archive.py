# cursor.execute("SELECT FirstName + ' ' + LastName as 'EmployeeName' FROM Employees;")
# # row = cursor.fetchall()
# # print(row)
# #
# # cursor.execute("SELECT Address + ' ' + City + ' ' + Region + ' ' + PostalCode + ' ' + Country as 'Address' from Employees")
# # row = cursor.fetchall()
# # print(row)
# #
# # cursor.execute("SELECT TitleOfCourtesy + ' ' + FirstName + ' ' + LastName as 'Person', City FROM Employees WHERE country = 'UK'")
# # row = cursor.fetchall()
# # print(row)
#
# # This is better than fetchall because its printing one row at a time unlike
# # Fetchall which gets all at once
# for row in cursor:
#     print(row)

# cursor.execute("SELECT * FROM Products;")
#
# # for row in cursor:
# #     print(row.UnitPrice)
#
# # for row in cursor:
# #     print(type(row))
#
# while True:
#     record = cursor.fetchone()
#     if record is None:
#         break
#     else:
#         print(type(record))
#         print(record.UnitPrice)
#
# query = """
#         SELECT CategoryID
#         , AVG(UnitPrice) AS AvgPrice
#         FROM Products
#         GROUP BY CategoryID
#         """
#
# cursor.execute(query)
# for row in cursor:
#     print(row.CategoryID, row.AvgPrice)