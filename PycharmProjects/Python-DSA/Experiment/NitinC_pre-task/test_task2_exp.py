import json
import pytest
import requests
import logging
import subprocess

from PycharmProjects.Utility import basicUtility, sqlUtility

obj = basicUtility.Library()
sqlGateway = sqlUtility.Sql("localhost", "root", "new_password", "db1")

log_file_path = 'my_log_file.log'
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(levelname)s: %(message)s')

# Run the secondary_script.py file
subprocess.run(["python", "exp.py"])


@pytest.mark.automate
@pytest.mark.parametrize(
    "productId", ["1225", "3674", "2585", "8739", "4643"]
)
@pytest.mark.run(order=5)
def test_automate_add_items_to_a_single_cart(productId):
    logging.info("automated addition for cartId: %s", obj.getCartId())
    obj.log_message("info",f"automated addition for cartId: {obj.getCartId()}")

    value = add_items_to_cart(productId)

    # #soft assertion -> adding failure points to data structure or we can log them
    if not value:
       obj.addMessageToQueue(f"Error occurred in add_items_to_cart with productId: {productId}")


    assert value, f"Error occurred in add_items_to_cart with productId: {productId} {value}"

@pytest.mark.automate
@pytest.mark.run(order=7)
def test_automate_create_cart_add_items_to_cart_create_an_order():
    count = 1

    while count <= 5:
        test_create_cart()
        productIds = ["1225", "3674", "2585", "8739", "4643"]

        for i in range(0, len(productIds)):
            test_automate_add_items_to_a_single_cart(productIds[i])

        test_create_new_order()
        logging.info("End to end automation testing %d", count)
        logging.info("============================================================")
        count += 1


@pytest.mark.run(order=1)
def test_checkAPIStatus():
    expectedStatusCode = 200
    response = requests.get(obj.checkUrlStatusAPI())

    assert response.status_code == expectedStatusCode


@pytest.mark.run(order=2)
def test_getProductById():
    productId = 1225
    expectedManufacturer = "Bosch"
    response = requests.get(obj.getProductByIdAPI(productId))
    jsonResponse = json.loads(response.text)
    manufacturer = jsonResponse['manufacturer']

    assert response.status_code == 200
    assert manufacturer == expectedManufacturer


@pytest.mark.run(order=3)
def test_create_cart():
    expectedCreatedResoponse = True

    response = requests.post(obj.createCartAPI())
    jsonResponse = json.loads(response.text)
    created = jsonResponse['created']
    cartId = jsonResponse['cartId']
    logging.info("Cart created with cartId: ", cartId)
    obj.setCartId(cartId)
    # logging.info("Check: ", response.text)

    # DB
    sqlGateway.add_TableOne_Info(cartId)

    assert created == expectedCreatedResoponse


@pytest.mark.run(order=4)
def test_add_items_to_cart():
    expectedStatusCodeResponse = 201
    productId = 1225

    url = obj.addItemToCartAPI(obj.getCartId())
    jsonPayload = dynamic_add_items_to_cart_file_handling(productId)
    response = requests.request("POST", url, headers=obj.header_with_content_type(), data=jsonPayload, timeout=30)
    # print("Current Check: ", response.text)

    # DB
    sqlGateway.add_TableTwo_Info(str(productId), obj.getCartId())
    logging.info(f"CartId: {obj.getCartId()} with productId: {productId} persisted to tableTwo.")

    assert response.status_code == expectedStatusCodeResponse


# @pytest.mark.parametrize(
#     productId=["1225", "3674", "2585", "8739", "4643", "4646"],
#     customerName=["Afzhal", "Nitin Chawala", "Shubham", "Mriganka", "Gaurav"]
# )
# def test_exp_automation_method(productId, customerName):


@pytest.mark.run(order=6)
def test_create_new_order():
    url = obj.createNewOrderAPI()
    jsonPayload = dynamic_create_order_file_handling()
    response = requests.request("POST", url, headers=obj.header_with_content_type(), data=jsonPayload, timeout=30)

    pythonResponseFormat = json.loads(response.text)
    orderId = pythonResponseFormat["orderId"]
    pythonFormatJsonPayload = json.loads(jsonPayload)
    cartId = pythonFormatJsonPayload["cartId"]
    customerName = pythonFormatJsonPayload["customerName"]

    #DB
    sqlGateway.add_TableThree_Info(orderId, cartId, customerName)
    logging.info(f"OrderId: {orderId} with cartId: {cartId} with customer name: {customerName}")
    assert response.status_code == 201

    logging.info("New Order created: ", response.text)


def dynamic_add_items_to_cart_file_handling(productId):
    file = open("/home/afzhal-ahmed-s/PycharmProjects/add_item_to_cart_payload.json", 'r')
    jsonPayload = json.loads(file.read())

    jsonPayload["productId"] = str(productId)
    jsonPayload = json.dumps(jsonPayload)
    return jsonPayload


def dynamic_create_order_file_handling():
    file = open("/home/afzhal-ahmed-s/PycharmProjects/create_order_payload.json", 'r')
    jsonPayload = json.loads(file.read())

    jsonPayload["cartId"] = obj.getCartId()
    jsonPayload["customerName"] = obj.generate_random_name()

    jsonPayload = json.dumps(jsonPayload)

    return jsonPayload


def add_items_to_cart(productId):
    url = obj.addItemToCartAPI(obj.getCartId())
    file = open("/home/afzhal-ahmed-s/PycharmProjects/add_item_to_cart_payload.json", 'r')
    jsonPayload = json.loads(file.read())

    jsonPayload["productId"] = str(productId)
    jsonPayload = json.dumps(jsonPayload)

    response = requests.request("POST", url, headers=obj.header_with_content_type(), data=jsonPayload, timeout=30)
    jsonResponse = json.loads(response.text)
    # print(response.text)

    #DB
    sqlGateway.add_TableTwo_Info(productId, obj.getCartId())
    logging.info(f"CartId: {obj.getCartId()} with productId: {productId} persisted to tableTwo.")

    if "created" in jsonResponse:
        return True
    else:
        return False


# soft assertion explanation
def test_give_me_all_messages_in_queues():
    obj.getAllMessageFromQueues()





