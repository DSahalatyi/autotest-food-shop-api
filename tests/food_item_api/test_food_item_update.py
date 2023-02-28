from pathlib import Path

import pytest


pytestmark = [pytest.mark.food_item_update, pytest.mark.usefixtures("create_test_food_item")]


BASE_DIR = Path(__file__).parent.parent
image = [('file', ('test.png', open(BASE_DIR/'src/data/test.png', 'rb'), 'image/png'))]
update_image = [('file', ('test.png', open(BASE_DIR/'src/data/test.png', 'rb'), 'image/png'))]


@pytest.mark.tcid80
def test_attempt_update_food_item_with_random_token(client_random_token, random_food_item_info, db_utility):
    food_section_id = list(db_utility.foodsections.find({}))[0]["_id"]
    random_food_item_info["food-section"] = str(food_section_id)
    initial_food_item = list(db_utility.fooditems.find({}))[0]
    response = client_random_token.post(
        f"api/food-item/{initial_food_item['_id']}/update", data=random_food_item_info, files=image
    )
    assert response.status_code == 405
    db_food_items = list(db_utility.fooditems.find({}))
    assert len(db_food_items) == 1
    assert db_food_items[0]["name"] == initial_food_item["name"]


@pytest.mark.tcid81
def test_update_food_item(client_is_staff_token, random_food_item_info, db_utility):
    food_section_id = list(db_utility.foodsections.find({}))[1]["_id"]
    random_food_item_info["food_section"] = str(food_section_id)
    random_food_item_info["image"] = update_image[0][1][0]
    initial_food_item = list(db_utility.fooditems.find({}))[0]
    response = client_is_staff_token.post(
        f"api/food-item/{initial_food_item['_id']}/update", data=random_food_item_info, files=update_image
    )
    assert response.status_code == 200
    db_food_items = list(db_utility.fooditems.find())
    assert db_food_items[0]["name"] == random_food_item_info["name"]
    assert db_food_items[0]["ordering_priority"] == random_food_item_info["ordering_priority"]
    assert str(db_food_items[0]["food_section"]) == random_food_item_info["food_section"]
    assert db_food_items[0]["image"] == random_food_item_info["image"]
    assert float(db_food_items[0]["price"].to_decimal()) == random_food_item_info["price"]


@pytest.mark.tcid82
@pytest.mark.usefixtures("create_random_food_item")
def test_attempt_update_food_item_with_existing_name(
        client_is_staff_token, test_food_item_info, random_food_item_info, db_utility
):
    initial_food_item = list(db_utility.fooditems.find({}))[0]
    response = client_is_staff_token.post(
        f"api/food-item/{initial_food_item['_id']}/update", data=test_food_item_info, files=image
    )
    assert response.status_code == 500
    db_food_items = list(db_utility.fooditems.find({}))
    assert db_food_items[0]["name"] == initial_food_item["name"]


@pytest.mark.tcid83
@pytest.mark.usefixtures("create_test_food_item")
def test_attempt_update_food_item_with_empty_name(client_is_staff_token, test_food_item_info, db_utility):
    test_food_item_info["name"] = ''
    initial_food_item = list(db_utility.fooditems.find({}))[0]
    response = client_is_staff_token.post(
        f"api/food-item/{initial_food_item['_id']}/update", data=test_food_item_info, files=image
    )
    assert response.status_code == 409
    db_food_items = list(db_utility.fooditems.find({}))
    assert db_food_items[0]["name"] == initial_food_item["name"]


@pytest.mark.tcid84
@pytest.mark.usefixtures("create_test_food_item")
def test_attempt_update_food_item_with_empty_food_section(client_is_staff_token, test_food_item_info, db_utility):
    test_food_item_info["food_section"] = ''
    initial_food_item = list(db_utility.fooditems.find({}))[0]
    response = client_is_staff_token.post(
        f"api/food-item/{initial_food_item['_id']}/update", data=test_food_item_info, files=image
    )
    assert response.status_code == 409
    db_food_items = list(db_utility.fooditems.find({}))
    assert db_food_items[0]["food_section"] == initial_food_item["food_section"]


@pytest.mark.tcid85
@pytest.mark.usefixtures("create_test_food_item")
def test_attempt_update_food_item_with_empty_ordering_priority(client_is_staff_token, test_food_item_info, db_utility):
    test_food_item_info["ordering_priority"] = ''
    initial_food_item = list(db_utility.fooditems.find({}))[0]
    response = client_is_staff_token.post(
        f"api/food-item/{initial_food_item['_id']}/update", data=test_food_item_info, files=image
    )
    assert response.status_code == 409
    db_food_items = list(db_utility.fooditems.find({}))
    assert db_food_items[0]["ordering_priority"] == initial_food_item["ordering_priority"]


@pytest.mark.tcid86
@pytest.mark.usefixtures("create_test_food_item")
def test_attempt_update_food_item_with_empty_image(client_is_staff_token, test_food_item_info, db_utility):
    test_food_item_info["image"] = ''
    initial_food_item = list(db_utility.fooditems.find({}))[0]
    response = client_is_staff_token.post(
        f"api/food-item/{initial_food_item['_id']}/update", data=test_food_item_info, files=image
    )
    assert response.status_code == 409
    db_food_items = list(db_utility.fooditems.find({}))
    assert db_food_items[0]["image"] == initial_food_item["image"]


@pytest.mark.tcid87
@pytest.mark.usefixtures("create_test_food_item")
def test_attempt_update_food_item_with_empty_price(client_is_staff_token, test_food_item_info, db_utility):
    test_food_item_info["price"] = ''
    initial_food_item = list(db_utility.fooditems.find({}))[0]
    response = client_is_staff_token.post(
        f"api/food-item/{initial_food_item['_id']}/update", data=test_food_item_info, files=image
    )
    assert response.status_code == 500
    db_food_items = list(db_utility.fooditems.find({}))
    assert db_food_items[0]["price"] == initial_food_item["price"]


@pytest.mark.tcid88
@pytest.mark.usefixtures("create_test_food_item")
def test_attempt_update_food_item_with_empty_is_available(client_is_staff_token, test_food_item_info, db_utility):
    test_food_item_info["is_available"] = ''
    initial_food_item = list(db_utility.fooditems.find({}))[0]
    response = client_is_staff_token.post(
        f"api/food-item/{initial_food_item['_id']}/update", data=test_food_item_info, files=image
    )
    assert response.status_code == 409
    db_food_items = list(db_utility.fooditems.find({}))
    assert db_food_items[0]["is_available"] == initial_food_item["is_available"]


@pytest.mark.tcid89
@pytest.mark.skip(reason="crashes server")
@pytest.mark.usefixtures("create_test_food_item")
def test_attempt_update_food_item_with_image_name_mismatch(client_is_staff_token, test_food_item_info, db_utility):
    test_food_item_info["image"] = "image.png"
    initial_food_item = list(db_utility.fooditems.find({}))[0]
    import pdb;pdb.set_trace()
    response = client_is_staff_token.post(
        f"api/food-item/{initial_food_item['_id']}/update", data=test_food_item_info, files=update_image
    )
    import pdb; pdb.set_trace()
    assert response.status_code == 200