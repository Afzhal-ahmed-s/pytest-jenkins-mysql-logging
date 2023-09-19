import json
import pytest
import requests
import logging
import sys
import pypandoc
from pycharm_projects.utility import basic_utility, sql_utility, kafka_utility
import subprocess
import datetime

# Define the timestamp variable
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


input_file = "/home/afzhal-ahmed-s/pytest-jenkins-mysql-logging/pycharm_projects/task/demonstration/nitinc_pre_task/log_file.log"
output_file = "output.html"

sys.path.append('/home/afzhal-ahmed-s/pytest_jenkins_mysql_logging/pycharm_projects')

obj = basic_utility.Basic_utility()
sql_gateway = sql_utility.Sql_utility("localhost", "root", "new_password", "db1")
# kafka utility
kafka_utility = kafka_utility.Kafka_utility()
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


@pytest.mark.automate
@pytest.mark.parametrize(
    "product_id", ["1225", "3674", "2585", "8739", "4643"]
)
@pytest.mark.run(order=5)
def test_automate_add_items_to_a_single_cart(product_id):
    logging.info("automated addition for cartId: %s", obj.get_cart_id())
    obj.log_message("info", f"automated addition for cartId: {obj.get_cart_id()}")

    value = add_items_to_cart(product_id)

    # soft assertion -> adding failure points to data structure, or we can log them
    if not value:
        obj.add_message_to_queue(f"Error occurred in add_items_to_cart with productId: {product_id}")
        logging.warning(f"Error occurred in add_items_to_cart with productId: {product_id}")

        assert value, f"Error occurred in add_items_to_cart with productId: {product_id} {value}"

    else:
        logging.info(f"Product with productId- {product_id} added to cart with cartId- {obj.get_cart_id()}"
                     f" in test_automate_add_items_to_a_single_cart")
        assert value, (f"Product with productId- {product_id} added to cart with cartId- {obj.get_cart_id()} "
                       f"in test_automate_add_items_to_a_single_cart")


@pytest.mark.automate
@pytest.mark.run(order=7)
def test_automate_create_cart_add_items_to_cart_create_an_order():
    count = 1

    while count <= 5:
        test_create_cart()
        product_ids = ["1225", "3674", "2585", "8739", "4643"]

        for i in range(0, len(product_ids)):
            test_automate_add_items_to_a_single_cart(product_ids[i])

        test_create_new_order()
        logging.info("End to end automation testing %d", count)
        logging.info("============================================================")
        count += 1


@pytest.mark.run(order=1)
def test_check_api_status():
    expected_status_code = 200
    response = requests.get(obj.check_url_status_api())

    # kafka
    message = str(response.status_code)
    kafka_utility.produce_message("test_check_api_status: ", message)
    logging.info("test_check_api_status message inserted into kafka topic 'noduco-task' via producer.")

    assert response.status_code == expected_status_code


@pytest.mark.run(order=2)
def test_get_product_by_id():
    product_id = 1225
    expected_manufacturer = "Bosch"
    response = requests.get(obj.get_product_by_id_api(product_id))
    json_response = json.loads(response.text)
    manufacturer = json_response['manufacturer']

    # kafka
    message = response.text
    kafka_utility.produce_message("test_get_product_by_id: ", message)
    logging.info("test_get_product_by_id inserted into kafka topic 'noduco-task' via producer.")

    assert response.status_code == 200
    assert manufacturer == expected_manufacturer


@pytest.mark.run(order=3)
def test_create_cart():
    expected_created_response = True

    response = requests.post(obj.create_cart_api())
    json_response = json.loads(response.text)
    created = json_response['created']
    cartId = json_response['cartId']
    logging.info(f"Cart created with cartId: {cartId}")
    obj.set_cart_id(cartId)

    # DB
    sql_gateway.add_table_one_info(cartId)

    # kafka
    message = response.text
    kafka_utility.produce_message("test_create_cart: ", message)
    logging.info("test_create_cart inserted into kafka topic 'noduco-task' via producer.")

    assert created == expected_created_response


@pytest.mark.run(order=4)
def test_add_items_to_cart():
    expected_status_code_response = 201
    productId = 1225

    url = obj.add_item_to_cart_api(obj.get_cart_id())
    json_payload = dynamic_add_items_to_cart_file_handling(productId)
    response = requests.request("POST", url, headers=obj.header_with_content_type(), data=json_payload, timeout=30)

    # DB
    sql_gateway.add_table_two_info(str(productId), obj.get_cart_id())
    logging.info(f"CartId: {obj.get_cart_id()} with productId: {productId} persisted to tableTwo.")

    # kafka
    message = response.text
    kafka_utility.produce_message("test_add_items_to_cart: ", message)
    logging.info("test_add_items_to_cart inserted into kafka topic 'noduco-task' via producer.")

    assert response.status_code == expected_status_code_response


@pytest.mark.run(order=6)
def test_create_new_order():
    url = obj.create_new_order_api()
    json_payload = dynamic_create_order_file_handling()
    response = requests.request("POST", url, headers=obj.header_with_content_type(), data=json_payload, timeout=30)

    python_response_format = json.loads(response.text)
    orderId = python_response_format["orderId"]
    python_format_json_payload = json.loads(json_payload)
    cartId = python_format_json_payload["cartId"]
    customer_name = python_format_json_payload["customerName"]

    # DB
    sql_gateway.add_table_three_info(orderId, cartId, customer_name)
    logging.info(f"OrderId: {orderId} with cartId: {cartId} with customer name: {customer_name}")

    # kafka
    message = response.text
    kafka_utility.produce_message("test_create_new_order: ", message)
    logging.info("test_create_new_order inserted into kafka topic 'noduco-task' via producer.")

    assert response.status_code == 201

    logging.info(f"New Order created: {response.text}")


def dynamic_add_items_to_cart_file_handling(product_id):
    file = open("/home/afzhal-ahmed-s/PycharmProjects/add_item_to_cart_payload.json", 'r')
    json_payload = json.loads(file.read())

    json_payload["productId"] = str(product_id)
    json_payload = json.dumps(json_payload)
    return json_payload


def dynamic_create_order_file_handling():
    file = open("/home/afzhal-ahmed-s/PycharmProjects/create_order_payload.json", 'r')
    json_payload = json.loads(file.read())

    json_payload["cartId"] = obj.get_cart_id()
    json_payload["customerName"] = obj.generate_random_name()

    json_payload = json.dumps(json_payload)

    return json_payload


def add_items_to_cart(product_id):
    url = obj.add_item_to_cart_api(obj.get_cart_id())
    file = open("/home/afzhal-ahmed-s/PycharmProjects/add_item_to_cart_payload.json", 'r')
    json_payload = json.loads(file.read())

    json_payload["productId"] = str(product_id)
    json_payload = json.dumps(json_payload)

    response = requests.request("POST", url, headers=obj.header_with_content_type(), data=json_payload, timeout=30)
    json_response = json.loads(response.text)

    # DB
    sql_gateway.add_table_two_info(product_id, obj.get_cart_id())
    logging.info(f"CartId: {obj.get_cart_id()} with productId: {product_id} persisted to tableTwo.")

    if "created" in json_response:
        return True
    else:
        return False


# soft assertion explanation
def test_give_me_all_messages_in_queues_and_kafka_consumer():
    obj.get_all_message_from_queues()
    kafka_utility.consume_message()


def test_convert_log_file_to_html():
    subprocess.run(["pandoc", input_file, "-o", output_file])

# pre-Sep15
# [DONE] logs -> html format (python library)
# [DONE] data_driven ->  i) test_excel_to_json_payload_then_api_request
#                        ii)test_list_of_json_to_excel_data_insertion

# Sep15
# extend report html else alternative, generate html report for test suite, try to host it, for history of 7 days
# next call on google meet