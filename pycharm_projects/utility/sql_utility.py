import mysql.connector
import logging


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
