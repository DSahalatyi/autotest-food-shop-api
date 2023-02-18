import pytest

pytestmark = pytest.mark.user_find


@pytest.mark.tcid44
def test_attempt_user_find_with_random_token(client_random_token, db_utility):
    user_id = list(db_utility.users.find({}))[0]["_id"]
    response = client_random_token.get(f"api/user/{user_id}/find")
    assert response.status_code == 405


@pytest.mark.tcid45
def test_find_user(client_is_staff_token, db_utility):
    user_id = list(db_utility.users.find({}))[0]["_id"]
    response = client_is_staff_token.get(f"api/user/{user_id}/find")
    assert response.status_code == 200
    db_users = list(db_utility.users.find({}))
    # Casting ObjectID to str for valid comparison
    db_users[0]["_id"] = str(db_users[0]["_id"])
    assert response.json()["item"] == db_users[0]
