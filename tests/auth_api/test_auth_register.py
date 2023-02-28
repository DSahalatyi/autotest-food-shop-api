import json

import pytest


pytestmark = pytest.mark.register


@pytest.mark.tcid1
def test_register_new_user_required_only(client, db_utility, random_user_info):
    response = client.post("api/auth/register", json=random_user_info)
    assert response.status_code == 201
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 1
    assert random_user_info["username"] == db_users[0]["username"]


@pytest.mark.tcid2
@pytest.mark.usefixtures("register_test_user")
def test_attempt_register_with_existing_username(client, db_utility, random_user_info):
    existing_user = list(db_utility.users.aggregate([{'$sample': {"size": 1}}]))
    random_user_info["username"] = existing_user[0]["username"]
    response = client.post("api/auth/register", json=random_user_info)
    assert response.status_code == 400
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 1
    assert db_users[0]["username"] == existing_user[0]["username"]


@pytest.mark.tcid3
@pytest.mark.usefixtures("register_test_user")
def test_attempt_register_with_existing_email(client, db_utility, random_user_info):
    existing_user = list(db_utility.users.aggregate([{'$sample': {"size": 1}}]))
    random_user_info["email"] = existing_user[0]["email"]
    response = client.post("api/auth/register", json=random_user_info)
    assert response.status_code == 400
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 1
    assert db_users[0]["email"] == existing_user[0]["email"]


@pytest.mark.tcid4
@pytest.mark.usefixtures("register_test_user")
def test_attempt_register_with_existing_phone_number(client, db_utility, random_user_info):
    existing_user = list(db_utility.users.aggregate([{'$sample': {"size": 1}}]))
    random_user_info["phone_number"] = existing_user[0]["phone_number"]
    response = client.post("api/auth/register", json=random_user_info)
    db_users = list(db_utility.database.users.find({}))
    assert response.status_code == 400
    assert len(db_users) == 1
    assert db_users[0]["phone_number"] == existing_user[0]["phone_number"]


@pytest.mark.tcid5
def test_attempt_register_with_empty_username(client, db_utility, random_user_info):
    random_user_info["username"] = ''
    response = client.post("api/auth/register", json=random_user_info)
    assert response.status_code == 409
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 0


@pytest.mark.tcid6
def test_attempt_register_with_empty_email(client, db_utility, random_user_info):
    random_user_info["email"] = ''
    response = client.post("api/auth/register", json=random_user_info)
    assert response.status_code == 409
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 0


@pytest.mark.tcid7
def test_attempt_register_with_empty_password(client, db_utility, random_user_info):
    random_user_info["password"] = ''
    response = client.post("api/auth/register", json=random_user_info)
    assert response.status_code == 409
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 0


@pytest.mark.tcid8
def test_attempt_register_with_empty_first_name(client, db_utility, random_user_info):
    random_user_info["first_name"] = ''
    response = client.post("api/auth/register", json=random_user_info)
    assert response.status_code == 409
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 0


@pytest.mark.tcid9
def test_attempt_register_with_empty_last_name(client, db_utility, random_user_info):
    random_user_info["last_name"] = ''
    response = client.post("api/auth/register", json=random_user_info)
    assert response.status_code == 409
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 0


@pytest.mark.tcid10
def test_attempt_register_with_empty_age(client, db_utility, random_user_info):
    random_user_info["age"] = ''
    response = client.post("api/auth/register", json=random_user_info)
    assert response.status_code == 409
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 0


@pytest.mark.tcid11
def test_attempt_register_with_empty_phone_number(client, db_utility, random_user_info):
    random_user_info["phone_number"] = ''
    response = client.post("api/auth/register", json=random_user_info)
    assert response.status_code == 409
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 0
