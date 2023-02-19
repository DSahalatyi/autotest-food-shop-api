import json

import pytest


pytestmark = [pytest.mark.food_item_create]


image = [('file', ('test.png',open('src/data/test.png', 'rb'), 'image/png'))]


@pytest.mark.tcid72
def test_attempt_create_food_item_with_random_token(client_random_token, test_food_item_info, db_utility):
    response = client_random_token.post("api/food-item/create", data=test_food_item_info, files=image)
    assert response.status_code == 405
    db_food_items = list(db_utility.fooditems.find({}))
    assert len(db_food_items) == 0


@pytest.mark.tcid73
def test_create_food_item(client_is_staff_token, random_food_item_info, db_utility):
    response = client_is_staff_token.post("api/food-item/create", data=random_food_item_info, files=image)
    assert response.status_code == 201
    db_food_items = list(db_utility.fooditems.find({}))
    # Removing food item ID from the dict for valid assertion
    assert db_food_items[0]["name"] == random_food_item_info["name"]
    assert str(db_food_items[0]["food_section"]) == random_food_item_info["food_section"]
    assert db_food_items[0]["ordering_priority"] == random_food_item_info["ordering_priority"]
    assert float(db_food_items[0]["price"].to_decimal()) == random_food_item_info["price"]
    assert db_food_items[0]["is_available"] == random_food_item_info["is_available"]


@pytest.mark.tcid74
@pytest.mark.usefixtures("create_random_food_item")
def test_attempt_create_food_item_with_existing_name(client_is_staff_token, test_food_item_info, db_utility):
    existing_food_item = list(db_utility.fooditems.find({}))[0]
    test_food_item_info["name"] = existing_food_item["name"]
    response = client_is_staff_token.post("api/food-item/create", data=test_food_item_info, files=image)
    assert response.status_code == 500
    db_food_items = list(db_utility.fooditems.find({}))
    assert len(db_food_items) == 1
    assert db_food_items[0]["name"] == existing_food_item["name"]


@pytest.mark.tcid75
@pytest.mark.usefixtures("create_test_food_section")
def test_attempt_create_food_item_with_empty_name(client_is_staff_token, test_food_item_info, db_utility):
    test_food_item_info["name"] = ''
    response = client_is_staff_token.post("api/food-item/create", data=test_food_item_info, files=image)
    assert response.status_code == 409
    db_food_items = list(db_utility.fooditems.find({}))
    assert len(db_food_items) == 0


@pytest.mark.tcid76
@pytest.mark.usefixtures("create_test_food_section")
def test_attempt_create_food_item_with_empty_ordering_priority(client_is_staff_token, test_food_item_info, db_utility):
    test_food_item_info["ordering_priority"] = ''
    response = client_is_staff_token.post("api/food-item/create", data=test_food_item_info, files=image)
    assert response.status_code == 409
    db_food_items = list(db_utility.fooditems.find({}))
    assert len(db_food_items) == 0


@pytest.mark.tcid77
@pytest.mark.usefixtures("create_test_food_section")
def test_attempt_create_food_item_with_empty_food_section(client_is_staff_token, test_food_item_info, db_utility):
    test_food_item_info["food_section"] = ""
    response = client_is_staff_token.post("api/food-item/create", data=test_food_item_info, files=image)
    assert response.status_code == 409
    db_food_items = list(db_utility.fooditems.find({}))
    assert len(db_food_items) == 0


@pytest.mark.tcid78
@pytest.mark.usefixtures("create_test_food_section")
def test_attempt_create_food_item_with_empty_image(
        client_is_staff_token, test_food_item_info, db_utility
):
    test_food_item_info["image"] = ''
    response = client_is_staff_token.post("api/food-item/create", data=test_food_item_info, files=image)
    assert response.status_code == 409
    db_food_items = list(db_utility.fooditems.find({}))
    assert len(db_food_items) == 0


@pytest.mark.tcid79
@pytest.mark.xfail
@pytest.mark.usefixtures("create_test_food_section")
def test_attempt_create_food_item_with_empty_price(
        client_is_staff_token, test_food_item_info, db_utility
):
    test_food_item_info["price"] = ''
    response = client_is_staff_token.post("api/food-item/create", data=test_food_item_info, files=image)
    assert response.status_code == 409
    db_food_items = list(db_utility.fooditems.find({}))
    assert len(db_food_items) == 0