import json
import requests
from faker import Faker
import queue
import logging


class Basic_utility:

    def __init__(self):
        global base_url
        global soft_assert_queue_1
        soft_assert_queue_1 = queue.Queue()

        self.cart_id = 0
        base_url = "https://simple-grocery-store-api.glitch.me"
        logging.info("Library object created.")

    def check_if_element_is_present_in_the_list(self, my_element, input_list):
        assert my_element in input_list, f"{my_element} not found in {input_list}"

    def header_with_access_token(self):
        return {"Authorization": "Bearer 3da66c8dc837414e2ba267151263f10147559f49a22e9e4b7f9314fec51d2541"}

    def get_base_url(self):
        return base_url

    def check_url_status_api(self):
        endpoint = "/status"
        return self.get_base_url() + endpoint

    def get_product_by_id_api(self, productId):
        endpoint = "/products/" + str(productId)
        return self.get_base_url() + endpoint

    def create_cart_api(self):
        endpoint = "/carts"
        return self.get_base_url() + endpoint

    def set_cart_id(self, input_cart_id):
        self.cart_id = input_cart_id

    def get_cart_id(self):
        return str(self.cart_id)

    def add_item_to_cart_api(self, cart_id):
        endpoint = ""

        if cart_id != None:
            endpoint = "/carts/" + str(cart_id) + "/items"
        else:
            endpoint = "/carts/" + str(self.cart_id) + "/items"

        return self.get_base_url() + endpoint

    def create_new_order_api(self):
        return self.get_base_url() + "/orders"

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

    def add_message_to_queue(self, message):
        soft_assert_queue_1.put(message)
        logging.warning(str(message))

    def retreive_message_from_queue(self):
        if not soft_assert_queue_1.empty():
            return soft_assert_queue_1.get()
        else:
            return False

    def get_all_message_from_queues(self):

        while not soft_assert_queue_1.empty():
            item = soft_assert_queue_1.get()
            print("From soft assertion:", item)
            logging.warning(f"From soft assertion: {item}")

