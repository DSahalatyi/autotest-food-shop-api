import json

import pytest


pytestmark = pytest.mark.login


@pytest.mark.tcid12
@pytest.mark.usefixtures("register_test_user")
def test_login_with_valid_data(client, db_utility):
    payload = {"username": "test_user", "password": "test_password"}
    response = client.post('api/auth/login', json=payload)
    assert response.status_code == 200
    db_users = list(db_utility.users.find({}))
    db_tokens = list(db_utility.tokens.find({}))
    assert len(db_tokens) == 1
    assert db_tokens[0]['refresh_token'][0] == json.load(response)['refreshToken']
    assert db_tokens[0]['user_id'] == db_users[0]['_id']


@pytest.mark.tcid13
@pytest.mark.usefixtures("register_test_user")
def test_login_with_empty_password(client, db_utility):
    payload = {"username": "test_user", "password": ''}
    response = client.post('api/auth/login', json=payload)
    assert response.status_code == 409
    db_tokens = list(db_utility.tokens.find({}))
    assert len(db_tokens) == 0


@pytest.mark.tcid14
@pytest.mark.usefixtures("register_test_user")
def test_login_with_wrong_password(client, db_utility):
    payload = {"username": "test_user", "password": 'test_password_'}
    response = client.post('api/auth/login', json=payload)
    assert response.status_code == 400
    db_tokens = list(db_utility.tokens.find({}))
    assert len(db_tokens) == 0


