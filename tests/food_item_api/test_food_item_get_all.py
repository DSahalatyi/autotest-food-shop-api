import pytest


pytestmark = pytest.mark.food_item_get_all


@pytest.mark.tcid90
@pytest.mark.usefixtures("create_test_food_item")
def test_attempt_food_item_get_all_with_random_token(client_random_token):
    response = client_random_token.get("api/food-item/get-all")
    assert response.status_code == 405


@pytest.mark.tcid91
@pytest.mark.usefixtures("create_test_food_item")
def test_food_item_get_all(client_is_staff_token, test_food_item_info, db_utility):
    response = client_is_staff_token.get("api/food-item/get-all")
    assert response.status_code == 200
    db_food_items = list(db_utility.fooditems.find({}))
    assert db_food_items[0]["name"] == test_food_item_info["name"]
    assert str(db_food_items[0]["food_section"]) == test_food_item_info["food_section"]
    assert db_food_items[0]["ordering_priority"] == test_food_item_info["ordering_priority"]
    assert db_food_items[0]["is_available"] == test_food_item_info["is_available"]
    assert float(db_food_items[0]["price"].to_decimal()) == test_food_item_info["price"]
    assert db_food_items[0]["image"] == test_food_item_info["image"]