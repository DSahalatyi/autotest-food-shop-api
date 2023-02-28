import json

import pytest


pytestmark = pytest.mark.create_user


@pytest.mark.tcid15
def test_attempt_create_user_with_random_token(client_random_token, test_user_info, db_utility):
    response = client_random_token.post("api/user/create", json=test_user_info)
    assert response.status_code == 405
    db_users = list(db_utility.users.find({}))
    assert len(db_users) == 1


@pytest.mark.tcid16
def test_create_new_user_required_only(client_is_staff_token, db_utility, random_user_info):
    response = client_is_staff_token.post("api/user/create", json=random_user_info)
    assert response.status_code == 201
    # Removing test_user from the database should leave only created user in db
    db_utility.users.delete_one({"username": {"$regex": "test_user"}})
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 1
    assert random_user_info["username"] == db_users[0]["username"]


@pytest.mark.tcid17
@pytest.mark.usefixtures("register_test_user")
def test_attempt_create_user_with_existing_username(client_is_staff_token, db_utility, random_user_info):
    existing_user = list(db_utility.users.aggregate([{'$sample': {"size": 1}}]))
    random_user_info["username"] = existing_user[0]["username"]
    response = client_is_staff_token.post("api/user/create", json=random_user_info)
    assert response.status_code == 400
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 1
    assert db_users[0]["username"] == existing_user[0]["username"]


@pytest.mark.tcid18
@pytest.mark.usefixtures("register_test_user")
def test_attempt_create_user_with_existing_email(client_is_staff_token, db_utility, random_user_info):
    existing_user = list(db_utility.users.aggregate([{'$sample': {"size": 1}}]))
    random_user_info["email"] = existing_user[0]["email"]
    response = client_is_staff_token.post("api/user/create", json=random_user_info)
    assert response.status_code == 400
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 1
    assert db_users[0]["username"] == existing_user[0]["username"]


@pytest.mark.tcid19
@pytest.mark.usefixtures("register_test_user")
def test_attempt_create_user_with_existing_phone_number(client_is_staff_token, db_utility, random_user_info):
    existing_user = list(db_utility.users.aggregate([{'$sample': {"size": 1}}]))
    random_user_info["phone_number"] = existing_user[0]["phone_number"]
    response = client_is_staff_token.post("api/user/create", json=random_user_info)
    assert response.status_code == 400
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 1
    assert db_users[0]["username"] == existing_user[0]["username"]


@pytest.mark.tcid20
def test_attempt_create_user_with_empty_username(client_is_staff_token, db_utility, random_user_info):
    random_user_info["username"] = ''
    response = client_is_staff_token.post("api/user/create", json=random_user_info)
    assert response.status_code == 409
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 1


@pytest.mark.tcid21
def test_attempt_create_user_with_empty_email(client_is_staff_token, db_utility, random_user_info):
    random_user_info["email"] = ''
    response = client_is_staff_token.post("api/user/create", json=random_user_info)
    assert response.status_code == 409
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 1


@pytest.mark.tcid22
def test_attempt_create_user_with_empty_password(client_is_staff_token, db_utility, random_user_info):
    random_user_info["password"] = ''
    response = client_is_staff_token.post("api/user/create", json=random_user_info)
    assert response.status_code == 409
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 1


@pytest.mark.tcid23
def test_attempt_create_user_with_empty_first_name(client_is_staff_token, db_utility, random_user_info):
    random_user_info["first_name"] = ''
    response = client_is_staff_token.post("api/user/create", json=random_user_info)
    assert response.status_code == 409
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 1


@pytest.mark.tcid24
def test_attempt_create_user_with_empty_last_name(client_is_staff_token, db_utility, random_user_info):
    random_user_info["last_name"] = ''
    response = client_is_staff_token.post("api/user/create", json=random_user_info)
    assert response.status_code == 409
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 1


@pytest.mark.tcid25
def test_attempt_create_user_with_empty_age(client_is_staff_token, db_utility, random_user_info):
    random_user_info["age"] = ''
    response = client_is_staff_token.post("api/user/create", json=random_user_info)
    assert response.status_code == 409
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 1


@pytest.mark.tcid26
def test_attempt_create_user_with_empty_phone_number(client_is_staff_token, db_utility, random_user_info):
    random_user_info["phone_number"] = ''
    response = client_is_staff_token.post("api/user/create", json=random_user_info)
    assert response.status_code == 409
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 1
