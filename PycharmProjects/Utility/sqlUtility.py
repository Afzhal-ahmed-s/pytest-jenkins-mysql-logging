import mysql.connector

import logging


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


        def add_TableOne_Info(self, cartId):
            sqlQueryFormat = "INSERT INTO tableOne (cartId) VALUES (%s)"
            values = (cartId,)
            cursor.execute(sqlQueryFormat, values)
            connection.commit()
            logging.info(f"{cartId} inserted into TableOne!")


        def add_TableTwo_Info(self, productId, cartId):
            sqlQueryFormat = "INSERT INTO tableTwo (productId, cartId) VALUES (%s, %s)"
            values = (productId, cartId)
            cursor.execute(sqlQueryFormat, values)
            connection.commit()
            logging.info(f"{cartId} with productId: {productId} inserted into TableTwo!")


        def add_TableThree_Info(self, orderId, cartId, customerName):
            sqlQueryFormat = "INSERT INTO tableThree (orderId, cartId, customerName) VALUES (%s, %s, %s)"
            values = (orderId, cartId, customerName)
            cursor.execute(sqlQueryFormat, values)
            connection.commit()
            logging.info(f"{cartId} with orderId: {orderId} with customer name: {customerName} inserted into TableThree!")