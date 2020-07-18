import pyodbc

class NWProducts:
    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.connection_string = "DRIVER={ODBC Driver 17 for SQL Server};"
        self.connection_string += f"SERVER={self.server};"
        self.connection_string += f"DATABASE={self.database};"
        self.connection_string += f"UID={self.username};"
        self.connection_string += f"PWD={self.password}"

        self.docker_northwind = pyodbc.connect(self.connection_string)
        self.cursor = self.docker_northwind.cursor()

    def _sql_query(self, sql_query):
        return self.cursor.execute(sql_query)

    def average_unit_price(self):
        records = self._sql_query("SELECT * FROM Products")
        unit_price = []
        for row in records:
            unit_price.append(row.UnitPrice)
        avg_unit_price = sum(unit_price)/len(unit_price)
        return avg_unit_price

# Test the class code
if __name__ == "__main__":
    sql_test = NWProducts()
    print(sql_test.average_unit_price())

