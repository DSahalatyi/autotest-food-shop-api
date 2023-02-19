import pytest


pytestmark = pytest.mark.food_item_find


@pytest.mark.tcid92
@pytest.mark.usefixtures("create_test_food_item")
def test_attempt_food_item_find_with_random_token(client_random_token, db_utility):
    food_item_id = list(db_utility.fooditems.find({}))[0]["_id"]
    response = client_random_token.get(f"api/food-item/{food_item_id}/find")
    assert response.status_code == 405


@pytest.mark.tcid93
@pytest.mark.usefixtures("create_test_food_item")
def test_find_food_item(client_is_staff_token, db_utility):
    food_item_id = list(db_utility.fooditems.find({}))[0]["_id"]
    response = client_is_staff_token.get(f"api/food-item/{food_item_id}/find")
    assert response.status_code == 200
    rs_food_item = response.json()["item"]
    db_food_items = list(db_utility.fooditems.find({}))
    # Casting values to basic data types for valid comparison
    db_food_items[0]["_id"] = str(db_food_items[0]["_id"])
    db_food_items[0]["food_section"] = str(db_food_items[0]["food_section"])
    db_food_items[0]["price"] = float(db_food_items[0]["price"].to_decimal())
    rs_food_item["price"] = float(rs_food_item["price"]["$numberDecimal"])
    assert db_food_items[0] == rs_food_item
