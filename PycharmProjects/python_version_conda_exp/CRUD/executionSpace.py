import Library as lib

obj = lib.Sql("localhost", "root", "new_password", "db1")
# Example usage
obj.create_employee("Afzhal", "Ahmed", 24, "afzhal.ahmeds@gmail.com")
obj.read_employees()
obj.update_employee_email(1, "updated.email@example.com")
obj.delete_employee(2)

# final steps
# Close cursor and connection
obj.close_cursor()
obj.close_connection()
