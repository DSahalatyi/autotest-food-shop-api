import json

import pytest

pytestmark = pytest.mark.update_food_section


@pytest.mark.tcid57
@pytest.mark.usefixtures("create_random_food_section")
def test_attempt_update_food_section_with_random_token(
        client_random_token, random_food_section_info, test_food_section_info, db_utility
):
    food_section_id = list(db_utility.foodsections.find({}))[0]["_id"]
    response = client_random_token.post(f"api/food-section/{food_section_id}/update", json=test_food_section_info)
    assert response.status_code == 405
    db_food_sections = list(db_utility.foodsections.find({}))
    assert db_food_sections[0]["name"] == random_food_section_info["name"]
    assert db_food_sections[0]["ordering_priority"] == random_food_section_info["ordering_priority"]
    assert db_food_sections[0]["is_available"] == random_food_section_info["is_available"]


@pytest.mark.tcid58
@pytest.mark.usefixtures("create_random_food_section")
def test_update_food_section(
        client_is_staff_token, random_food_section_info, test_food_section_info, db_utility
):
    food_section_id = list(db_utility.foodsections.find({}))[0]["_id"]
    response = client_is_staff_token.post(f"api/food-section/{food_section_id}/update", json=test_food_section_info)
    assert response.status_code == 200
    db_food_sections = list(db_utility.foodsections.find({}))
    assert db_food_sections[0]["name"] == test_food_section_info["name"]
    assert db_food_sections[0]["ordering_priority"] == test_food_section_info["ordering_priority"]
    assert db_food_sections[0]["is_available"] == test_food_section_info["is_available"]


@pytest.mark.tcid59
@pytest.mark.usefixtures("create_test_food_section")
@pytest.mark.usefixtures("create_random_food_section")
def test_update_food_section_with_existing_name(client_is_staff_token, test_food_section_info, db_utility):
    existing_food_section = list(db_utility.foodsections.find({}))[0]
    initial_name = existing_food_section["name"]
    response = client_is_staff_token.post(
        f"api/food-section/{existing_food_section['_id']}/update", json=test_food_section_info
    )
    assert response.status_code == 500
    db_food_section = list(db_utility.foodsections.find({}))
    assert db_food_section[0]["name"] == initial_name


@pytest.mark.tcid60
@pytest.mark.usefixtures("create_test_food_section")
@pytest.mark.usefixtures("create_random_food_section")
def test_update_food_section_with_existing_ordering_priority(client_is_staff_token, test_food_section_info, db_utility):
    existing_food_section = list(db_utility.foodsections.find({}))[0]
    initial_ordering_priority = existing_food_section["ordering_priority"]
    response = client_is_staff_token.post(
        f"api/food-section/{existing_food_section['_id']}/update", json=test_food_section_info
    )
    assert response.status_code == 500
    db_food_section = list(db_utility.foodsections.find({}))
    assert db_food_section[0]["ordering_priority"] == initial_ordering_priority


@pytest.mark.tcid62
@pytest.mark.usefixtures("create_test_food_section")
def test_update_food_section_with_empty_name(
        client_is_staff_token, random_food_section_info, test_food_section_info, db_utility):
    food_section_id = list(db_utility.foodsections.find({}))[0]["_id"]
    random_food_section_info["name"] = ''
    response = client_is_staff_token.post(
        f"api/food-section/{food_section_id}/update", json=random_food_section_info
    )
    assert response.status_code == 409
    db_food_sections = list(db_utility.foodsections.find({}))
    assert db_food_sections[0]["name"] == test_food_section_info['name']


@pytest.mark.tcid63
@pytest.mark.usefixtures("create_test_food_section")
def test_update_food_section_with_empty_ordering_priority(
        client_is_staff_token, random_food_section_info, test_food_section_info, db_utility):
    food_section_id = list(db_utility.foodsections.find({}))[0]["_id"]
    random_food_section_info["ordering_priority"] = ''
    response = client_is_staff_token.post(
        f"api/food-section/{food_section_id}/update", json=random_food_section_info
    )
    assert response.status_code == 409
    db_food_sections = list(db_utility.foodsections.find({}))
    assert db_food_sections[0]["ordering_priority"] == test_food_section_info['ordering_priority']


@pytest.mark.tcid65
@pytest.mark.usefixtures("create_test_food_section")
def test_update_food_section_with_empty_is_available(
        client_is_staff_token, random_food_section_info, test_food_section_info, db_utility):
    food_section_id = list(db_utility.foodsections.find({}))[0]["_id"]
    random_food_section_info["is_available"] = ''
    response = client_is_staff_token.post(
        f"api/food-section/{food_section_id}/update", json=random_food_section_info
    )
    assert response.status_code == 409
    db_food_sections = list(db_utility.foodsections.find({}))
    assert db_food_sections[0]["is_available"] == test_food_section_info["is_available"]
