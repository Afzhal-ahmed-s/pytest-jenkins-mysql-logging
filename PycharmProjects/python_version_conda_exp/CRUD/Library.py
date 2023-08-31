import mysql.connector

# Connect to the MySQL server
class Sql:

        def __init__(self, host, userName, password, database):
            global  connection
            connection = mysql.connector.connect(
                host= host,
                user= userName,
                password= password,
                database= database
            )
            # Creating a cursor
            global cursor
            cursor = connection.cursor()


        def create_employee(self, first_name, last_name, age, email):
            sqlQueryFormat = "INSERT INTO employees (first_name, last_name, age, email) VALUES (%s, %s, %s, %s)"
            values = (first_name, last_name, age, email)
            cursor.execute(sqlQueryFormat, values)
            connection.commit()
            print("Employee created!")

        def read_employees(self):
            sqlQuery = "SELECT * FROM employees"
            cursor.execute(sqlQuery)
            employees = cursor.fetchall()
            for employee in employees:
                print(employee)

        def update_employee_email(self, employee_id, new_email):
            sqlQueryFormat = "UPDATE employees SET email = %d WHERE id = %d"
            values = (new_email, employee_id)
            cursor.execute(sqlQueryFormat, values)
            connection.commit()
            print("Employee's email updated!")

        def delete_employee(self, employee_id):
            sqlQueryFormat = "DELETE FROM employees WHERE id = %s"
            values = (employee_id,)
            cursor.execute(sqlQueryFormat, values)
            connection.commit()
            print("Employee deleted!")

        def close_cursor(self):
            cursor.close()

        def close_connection(self):
            connection.close()


