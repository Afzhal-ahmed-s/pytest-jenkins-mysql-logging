import json
import requests
from faker import Faker

import queue

import logging

# Configure the logging settings
log_file_path = 'my_log_file.log'
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(levelname)s: %(message)s')


class Library:

    def __init__(self):
        global baseUrl
        global softAssertQueue1
        softAssertQueue1 = queue.Queue()

        self.cartId = 0
        baseUrl = "https://simple-grocery-store-api.glitch.me"
        print("Library object created.")

    def checkIfelementIsPresentInTheList(self, myElement, inputList):
        assert myElement in inputList, f"{myElement} not found in {inputList}"

    def headerWithAccessToken(self):
        return {"Authorization": "Bearer 3da66c8dc837414e2ba267151263f10147559f49a22e9e4b7f9314fec51d2541"}

    def getBaseUrl(self):
        return baseUrl

    def checkUrlStatusAPI(self):
        endpoint = "/status"
        return self.getBaseUrl() + endpoint

    def getProductByIdAPI(self, productId):
        endpoint = "/products/" + str(productId)
        return self.getBaseUrl() + endpoint

    def createCartAPI(self):
        endpoint = "/carts"
        return self.getBaseUrl() + endpoint

    def setCartId(self, inputCartId):
        self.cartId = inputCartId

    def getCartId(self):
        return str(self.cartId)

    def addItemToCartAPI(self, cartId):
        endpoint = ""

        if cartId != None:
            endpoint = "/carts/" + str(cartId) + "/items"
        else:
            endpoint = "/carts/" + str(self.cartId) + "/items"

        return self.getBaseUrl() + endpoint

    def createNewOrderAPI(self):
        return self.getBaseUrl() + "/orders"

    def generate_random_name(self):
        fake = Faker()
        return fake.name()

    def header_with_content_type(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer 3da66c8dc837414e2ba267151263f10147559f49a22e9e4b7f9314fec51d2541'
        }

    def header_without_content_type(self):
        return {
            'Authorization': 'Bearer 3da66c8dc837414e2ba267151263f10147559f49a22e9e4b7f9314fec51d2541'
        }

    def log_message(self, type, message):
        if type == "info":
            logging.info(message)

    def addMessageToQueue(self, message):
        softAssertQueue1.put(message)
        logging.warning(str(message))

    def retreiveMessageFromQueue(self):
        if not softAssertQueue1.empty():
            return softAssertQueue1.get()
        else:
            return False

    def getAllMessageFromQueues(self):

        while not softAssertQueue1.empty():
            print("From soft assertion:", softAssertQueue1.get())

