import pytest

pytestmark = pytest.mark.update_user


@pytest.mark.tcid27
def test_attempt_update_user_with_random_token(client_random_token, random_user_info, test_user_info, db_utility):
    user_id = list(db_utility.users.find({}))[0]['_id']
    response = client_random_token.post(f"api/user/{user_id}/update", json=test_user_info)
    assert response.status_code == 405
    db_users = list(db_utility.users.find({}))
    assert db_users[0]["username"] == random_user_info["username"]
    assert db_users[0]["email"] == random_user_info["email"]
    assert db_users[0]["first_name"] == random_user_info["first_name"]
    assert db_users[0]["last_name"] == random_user_info["last_name"]
    assert db_users[0]["age"] == random_user_info["age"]
    assert db_users[0]["phone_number"] == random_user_info["phone_number"]


@pytest.mark.tcid28
def test_update_user_all_required(client_is_staff_token, db_utility, random_user_info):
    user_id = list(db_utility.users.find({}))[0]['_id']
    response = client_is_staff_token.post(f"api/user/{user_id}/update", json=random_user_info)
    assert response.status_code == 200
    db_users = list(db_utility.users.find({}))
    assert len(db_users) == 1
    assert db_users[0]["username"] == random_user_info["username"]


@pytest.mark.tcid29
@pytest.mark.usefixtures("register_random_user")
def test_update_user_with_existing_username(client_is_staff_token, db_utility, random_user_info):
    db_users = list(db_utility.users.find({}))
    initial_username = db_users[1]["username"]
    response = client_is_staff_token.post(f"api/user/{db_users[1]['_id']}/update", json=random_user_info)
    assert response.status_code == 500
    db_users = list(db_utility.users.find({}))
    assert len(db_users) == 2
    assert db_users[1]["username"] == initial_username


@pytest.mark.tcid30
@pytest.mark.usefixtures("register_random_user")
def test_update_user_with_existing_email(client_is_staff_token, db_utility, random_user_info):
    db_users = list(db_utility.users.find({}))
    initial_email = db_users[1]["email"]
    response = client_is_staff_token.post(f"api/user/{db_users[1]['_id']}/update", json=random_user_info)
    assert response.status_code == 500
    db_users = list(db_utility.users.find({}))
    assert len(db_users) == 2
    assert db_users[1]["email"] == initial_email


@pytest.mark.tcid31
@pytest.mark.usefixtures("register_random_user")
def test_update_user_with_existing_first_name(client_is_staff_token, db_utility, random_user_info):
    db_users = list(db_utility.users.find({}))
    initial_first_name = db_users[1]["first_name"]
    response = client_is_staff_token.post(f"api/user/{db_users[1]['_id']}/update", json=random_user_info)
    assert response.status_code == 500
    db_users = list(db_utility.users.find({}))
    assert len(db_users) == 2
    assert db_users[1]["first_name"] == initial_first_name


@pytest.mark.tcid32
@pytest.mark.usefixtures("register_random_user")
def test_update_user_with_existing_last_name(client_is_staff_token, db_utility, random_user_info):
    db_users = list(db_utility.users.find({}))
    initial_last_name = db_users[1]["last_name"]
    response = client_is_staff_token.post(f"api/user/{db_users[1]['_id']}/update", json=random_user_info)
    assert response.status_code == 500
    db_users = list(db_utility.users.find({}))
    assert len(db_users) == 2
    assert db_users[1]["last_name"] == initial_last_name


@pytest.mark.tcid33
@pytest.mark.usefixtures("register_random_user")
def test_update_user_with_existing_age(client_is_staff_token, db_utility, random_user_info):
    db_users = list(db_utility.users.find({}))
    initial_age = db_users[1]["age"]
    response = client_is_staff_token.post(f"api/user/{db_users[1]['_id']}/update", json=random_user_info)
    assert response.status_code == 500
    db_users = list(db_utility.users.find({}))
    assert len(db_users) == 2
    assert db_users[1]["age"] == initial_age


@pytest.mark.tcid34
@pytest.mark.usefixtures("register_random_user")
def test_update_user_with_existing_phone_number(client_is_staff_token, db_utility, random_user_info):
    db_users = list(db_utility.users.find({}))
    initial_phone_number = db_users[1]["phone_number"]
    response = client_is_staff_token.post(f"api/user/{db_users[1]['_id']}/update", json=random_user_info)
    assert response.status_code == 500
    db_users = list(db_utility.users.find({}))
    assert len(db_users) == 2
    assert db_users[1]["phone_number"] == initial_phone_number


@pytest.mark.tcid35
@pytest.mark.usefixtures("register_random_user")
def test_update_user_with_empty_username(client_is_staff_token, db_utility, random_user_info):
    db_users = list(db_utility.users.find({}))
    initial_username = db_users[1]["username"]
    random_user_info["username"] = ''
    response = client_is_staff_token.post(f"api/user/{db_users[1]['_id']}/update", json=random_user_info)
    assert response.status_code == 409
    db_users = list(db_utility.users.find({}))
    assert len(db_users) == 2
    assert db_users[1]["username"] == initial_username


@pytest.mark.tcid36
@pytest.mark.usefixtures("register_random_user")
def test_update_user_with_empty_email(client_is_staff_token, db_utility, random_user_info):
    db_users = list(db_utility.users.find({}))
    initial_email = db_users[1]["email"]
    random_user_info["email"] = ''
    response = client_is_staff_token.post(f"api/user/{db_users[1]['_id']}/update", json=random_user_info)
    assert response.status_code == 409
    db_users = list(db_utility.users.find({}))
    assert len(db_users) == 2
    assert db_users[1]["email"] == initial_email


@pytest.mark.tcid37
@pytest.mark.usefixtures("register_random_user")
def test_update_user_with_empty_password(client_is_staff_token, db_utility, random_user_info):
    db_users = list(db_utility.users.find({}))
    initial_password = db_users[1]["password"]
    random_user_info["password"] = ''
    response = client_is_staff_token.post(f"api/user/{db_users[1]['_id']}/update", json=random_user_info)
    assert response.status_code == 409
    db_users = list(db_utility.users.find({}))
    assert len(db_users) == 2
    assert db_users[1]["password"] == initial_password


@pytest.mark.tcid38
@pytest.mark.usefixtures("register_random_user")
def test_update_user_with_empty_first_name(client_is_staff_token, db_utility, random_user_info):
    db_users = list(db_utility.users.find({}))
    initial_first_name = db_users[1]["first_name"]
    random_user_info["first_name"] = ''
    response = client_is_staff_token.post(f"api/user/{db_users[1]['_id']}/update", json=random_user_info)
    assert response.status_code == 409
    db_users = list(db_utility.users.find({}))
    assert len(db_users) == 2
    assert db_users[1]["first_name"] == initial_first_name


@pytest.mark.tcid39
@pytest.mark.usefixtures("register_random_user")
def test_update_user_with_empty_last_name(client_is_staff_token, db_utility, random_user_info):
    db_users = list(db_utility.users.find({}))
    initial_last_name = db_users[1]["last_name"]
    random_user_info["last_name"] = ''
    response = client_is_staff_token.post(f"api/user/{db_users[1]['_id']}/update", json=random_user_info)
    assert response.status_code == 409
    db_users = list(db_utility.users.find({}))
    assert len(db_users) == 2
    assert db_users[1]["last_name"] == initial_last_name


@pytest.mark.tcid40
@pytest.mark.usefixtures("register_random_user")
def test_update_user_with_empty_age(client_is_staff_token, db_utility, random_user_info):
    db_users = list(db_utility.users.find({}))
    initial_age = db_users[1]["age"]
    random_user_info["age"] = ''
    response = client_is_staff_token.post(f"api/user/{db_users[1]['_id']}/update", json=random_user_info)
    assert response.status_code == 409
    db_users = list(db_utility.users.find({}))
    assert len(db_users) == 2
    assert db_users[1]["age"] == initial_age


@pytest.mark.tcid41
@pytest.mark.usefixtures("register_random_user")
def test_update_user_with_phone_number(client_is_staff_token, db_utility, random_user_info):
    db_users = list(db_utility.users.find({}))
    initial_phone_number = db_users[1]["phone_number"]
    random_user_info["age"] = ''
    response = client_is_staff_token.post(f"api/user/{db_users[1]['_id']}/update", json=random_user_info)
    assert response.status_code == 409
    db_users = list(db_utility.users.find({}))
    assert len(db_users) == 2
    assert db_users[1]["phone_number"] == initial_phone_number
