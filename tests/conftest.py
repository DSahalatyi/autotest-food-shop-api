import json
import os
from pathlib import Path

import httpx
import pytest
from dotenv import load_dotenv

from tests.src.utilities.db_utility import DBUtility
from tests.src.utilities.random_generator \
    import generate_random_user_info, generate_random_food_section_info, generate_random_food_item_info

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
BASE_DIR = Path(__file__).parent
image = [('file', ('test.png', open(BASE_DIR/'src/data/test.png', 'rb'), 'image/png'))]


@pytest.fixture(scope="module")
def client():
    with httpx.Client(base_url=BASE_URL) as client:
        yield client


@pytest.fixture(scope="function")
def client_is_staff_token(client, register_test_user):
    payload = {"username": "test_user", "password": "test_password"}
    response = client.post('api/auth/login', json=payload)
    with httpx.Client(base_url=BASE_URL) as client_is_staff:
        client_is_staff.headers.update({"authorization": f"Bearer {json.load(response)['accessToken']}"})
        yield client_is_staff


@pytest.fixture(scope="function")
def client_random_token(client, register_random_user, random_user_info):
    payload = {"username": random_user_info["username"], "password": random_user_info["password"]}
    response = client.post('api/auth/login', json=payload)
    with httpx.Client(base_url=BASE_URL) as random_client:
        random_client.headers.update({"authorization": f"Bearer {json.load(response)['accessToken']}"})
        yield random_client


@pytest.fixture(scope="function")
def random_user_info():
    yield generate_random_user_info()


@pytest.fixture(scope="function")
def test_user_info():
    payload = {
        "username": "test_user",
        "email": "test_email@g.com",
        "password": "test_password",
        "first_name": "Test",
        "last_name": "Test",
        "age": 20,
        "phone_number": "0123456789",
        "is_staff": True
    }
    yield payload


@pytest.fixture(scope="function")
def db_utility():
    db_utility = DBUtility()
    yield db_utility
    db_utility.clear_database()


@pytest.fixture(scope="function")
def register_test_user(client, test_user_info):
    yield client.post('api/auth/register', data=test_user_info)


@pytest.fixture(scope="function")
def register_random_user(client, random_user_info):
    yield client.post('api/auth/register', json=random_user_info)


@pytest.fixture(scope="function")
def test_food_section_info():
    payload = {
        "name": "Test-section",
        "ordering_priority": 1000,
        "is_available": True
    }
    yield payload


@pytest.fixture(scope="function")
def random_food_section_info():
    yield generate_random_food_section_info()


@pytest.fixture(scope="function")
def create_test_food_section(client_is_staff_token, test_food_section_info):
    client_is_staff_token.post("api/food-section/create", json=test_food_section_info)


@pytest.fixture(scope="function")
def create_random_food_section(client_is_staff_token, random_food_section_info):
    client_is_staff_token.post("api/food-section/create", json=random_food_section_info)


@pytest.fixture(scope="function")
def test_food_item_info(db_utility, create_test_food_section):
    payload = {
        "name": "Test_food_item",
        "food_section": "",
        "ordering_priority": 1000,
        "image": image[0][1][0],
        "price": 22.3,
        "is_available": True
    }
    food_section_id = list(db_utility.foodsections.find({}))[0]["_id"]
    payload["food_section"] = str(food_section_id)
    yield payload


@pytest.fixture(scope="function")
def create_test_food_item(client_is_staff_token, test_food_item_info):
    yield client_is_staff_token.post("api/food-item/create", data=test_food_item_info, files=image)


@pytest.fixture(scope="function")
def random_food_item_info(db_utility, create_random_food_section):
    food_item_info = generate_random_food_item_info()
    food_section_id = list(db_utility.foodsections.find({}))[0]["_id"]
    food_item_info["food_section"] = str(food_section_id)
    yield food_item_info


@pytest.fixture(scope="function")
def create_random_food_item(client_is_staff_token, random_food_item_info):
    yield client_is_staff_token.post("api/food-item/create", data=random_food_item_info, files=image)
