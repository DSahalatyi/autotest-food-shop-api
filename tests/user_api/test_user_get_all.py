import pytest

pytestmark = pytest.mark.user_get_all


@pytest.mark.tcid42
@pytest.mark.usefixtures("register_random_user")
def test_get_all_users(client_is_staff_token, random_user_info, db_utility):
    response = client_is_staff_token.get("api/user/get-all")
    assert response.status_code == 200
    db_users = list(db_utility.users.find({}))
    assert len(db_users) == 2
    assert db_users[1]["username"] == "test_user"
    assert db_users[0]["username"] == random_user_info["username"]


@pytest.mark.tcid43
@pytest.mark.usefixtures("db_utility")
def test_attempt_get_all_users_with_random_token(client_random_token):
    response = client_random_token.get("api/user/get-all")
    assert response.status_code == 405
