import os

import httpx
import pytest
from dotenv import load_dotenv

from src.utilities.db_utility import DBUtility
from src.utilities.random_generator \
    import generate_random_user_info

load_dotenv()

base_url = os.getenv("BASE_URL")


@pytest.fixture(scope="module")
def client():
    with httpx.Client(base_url=base_url) as client:
        yield client


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