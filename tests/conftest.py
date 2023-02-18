import json
import os

import httpx
import pytest
from dotenv import load_dotenv

from src.utilities.db_utility import DBUtility
from src.utilities.random_generator \
    import generate_random_user_info, generate_random_food_section_info

load_dotenv()

base_url = os.getenv("BASE_URL")


@pytest.fixture(scope="module")
def client():
    with httpx.Client(base_url=base_url) as client:
        yield client


@pytest.fixture(scope="function")
def client_is_staff_token(client, register_test_user):
    payload = {"username": "test_user", "password": "test_password"}
    response = client.post('api/auth/login', json=payload)
    with httpx.Client(base_url=base_url) as client_is_staff:
        client_is_staff.headers.update({"authorization": f"Bearer {json.load(response)['accessToken']}"})
        yield client_is_staff


@pytest.fixture(scope="function")
def client_random_token(client, register_random_user, random_user_info):
    payload = {"username": random_user_info["username"], "password": random_user_info["password"]}
    response = client.post('api/auth/login', json=payload)
    with httpx.Client(base_url=base_url) as random_client:
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
