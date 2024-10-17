import pyodbc 
def create_db_connection():
    try:
        connection_string=( 
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=DESKTOP-L9M362U\\SQL2024;"
            "Database=TechShop;"
            "TrustServerCertificate=yes;"
            "Trusted_Connection=yes;"
            "UID=sa;"
            "PWD=12345;"
            )
        conn=pyodbc.connect(connection_string)
        print (conn)
        return conn
    except Exception as e:
       print("Error while connecting to DB: {}", format(e))
conn=create_db_connection()



def insert_customer(self, customer):
    query = "INSERT INTO Customers (CustomerID, FirstName, LastName, Email, Phone, Address) VALUES (?, ?, ?, ?, ?, ?)"
    cursor = self.connection.cursor()
    cursor.execute(query, (customer.customer_id, customer.first_name, customer.last_name, customer.email, customer.phone, customer.address))
    self.connection.commit()



