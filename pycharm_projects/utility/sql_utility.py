import mysql.connector
import logging
import pycharm_projects.task.demonstration.nitinc_pre_task.reports as reports

# Connect to the MySQL server
class Sql_utility:

    def __init__(self, host, user_name, password, database):
        global connection
        connection = mysql.connector.connect(
            host=host,
            user=user_name,
            password=password,
            database=database
        )
        # Creating a cursor
        global cursor
        cursor = connection.cursor()

    def add_table_one_info(self, cart_id):
        sql_query_format = "INSERT INTO tableOne (cartId) VALUES (%s)"
        values = (cart_id,)
        cursor.execute(sql_query_format, values)
        connection.commit()
        logging.info(f"{cart_id} inserted into TableOne!")

    def add_table_two_info(self, product_id, cart_id):
        sql_query_format = "INSERT INTO tableTwo (productId, cartId) VALUES (%s, %s)"
        values = (product_id, cart_id)
        cursor.execute(sql_query_format, values)
        connection.commit()
        logging.info(f"{cart_id} with productId: {product_id} inserted into TableTwo!")

    def add_table_three_info(self, order_id, cart_id, customer_name):
        sql_query_format = "INSERT INTO tableThree (orderId, cartId, customerName) VALUES (%s, %s, %s)"
        values = (order_id, cart_id, customer_name)
        cursor.execute(sql_query_format, values)
        connection.commit()
        logging.info(
            f"{cart_id} with orderId: {order_id} with customer name: {customer_name} inserted into TableThree!")

    def add_report_info(self, time_stamp, html_file):
        sql_query_format = "INSERT INTO reports (timestamp, html_content) VALUES (?, ?)"
        values = (time_stamp, html_file)
        cursor.execute(sql_query_format, values)
        connection.commit()
        logging.info(
            f"HTML report generated at time: {time_stamp} inserted into reports table!")


    def persist_html_report_into_db(self, file_name):
        # Read the HTML file
        g_html_file_name = "/home/afzhal-ahmed-s/pytest-jenkins-mysql-logging/pycharm_projects/task/demonstration/nitinc_pre_task/reports/" + file_name + ".html"

        with open(g_html_file_name, 'r') as file:
            file_content = file.read()

        # Insert the file name and content into the database
        query = "INSERT INTO html_files (file_name, file_content) VALUES (%s, %s)"
        data = (file_name, file_content)

        cursor.execute(query, data)

        # Commit the transaction and close the connection
        connection.commit()
        connection.close()
        print(f"HTML file: '{file_name}.html' persisted into DB with file content: '{file_content}'.")


    def retrieve_html_data_from_db(self):
        try:
            query = "SELECT file_name, file_content FROM html_files"
            cursor.execute(query)

            # Fetch all the rows
            rows = cursor.fetchall()

            # # Process and print the retrieved data
            # for row in rows:
            #     file_name, file_content = row
            #     print(f"File Name: {file_name}")
            #     # You can use file_content for further processing or display
            #
            # # print(rows)

            return rows

        except mysql.connector.Error as error:
            print(f"Error: {error}")
            
        # finally:
        #     if connection.is_connected():
        #         # cursor.close()
        #         # connection.close()
        #         print("summa")
