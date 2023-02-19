import pytest


pytestmark = pytest.mark.food_item_delete


@pytest.mark.tcid94
@pytest.mark.usefixtures("create_test_food_item")
def test_attempt_delete_food_item_with_random_token(client_random_token, db_utility):
    food_item_id = list(db_utility.fooditems.find({}))[0]["_id"]
    response = client_random_token.get(f"api/food-item/{food_item_id}/delete")
    assert response.status_code == 405


@pytest.mark.tcid95
@pytest.mark.usefixtures("create_test_food_item", "create_random_food_item")
def test_delete_food_item(client_is_staff_token, random_food_item_info, db_utility):
    food_item_id = list(db_utility.fooditems.find({}))[0]["_id"]
    response = client_is_staff_token.get(f"api/food-item/{food_item_id}/delete")
    assert response.status_code == 200
    db_food_items = list(db_utility.fooditems.find({}))
    assert len(db_food_items) == 1
    assert db_food_items[0]["name"] == random_food_item_info["name"]
