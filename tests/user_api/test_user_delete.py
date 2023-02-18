import pytest

pytestmark = pytest.mark.user_delete


@pytest.mark.tcid46
@pytest.mark.usefixtures("register_test_user")
def test_attempt_delete_user_with_random_token(client_random_token, test_user_info, db_utility):
    user_id = list(db_utility.users.find({}))[0]["_id"]
    response = client_random_token.get(f"api/user/{user_id}/delete")
    assert response.status_code == 405
    db_users = list(db_utility.users.find({}))
    assert len(db_users) == 2
    assert db_users[0]["username"] == test_user_info["username"]


@pytest.mark.tcid47
def test_delete_user(client_is_staff_token, db_utility):
    user_id = list(db_utility.users.find({}))[0]["_id"]
    response = client_is_staff_token.get(f"api/user/{str(user_id)}/delete")
    assert response.status_code == 200
    db_users = list(db_utility.users.find({}))
    assert len(db_users) == 0
