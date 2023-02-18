import json

import pytest


pytestmark = pytest.mark.create_food_section


@pytest.mark.tcid48
def test_attempt_create_food_section_with_random_token(client_random_token, test_food_section_info, db_utility):
    response = client_random_token.post("api/food-section/create", json=test_food_section_info)
    assert response.status_code == 405
    db_food_sections = list(db_utility.foodsections.find({}))
    assert len(db_food_sections) == 0


@pytest.mark.tcid49
def test_create_new_food_section(client_is_staff_token, test_food_section_info, db_utility):
    response = client_is_staff_token.post("api/food-section/create", json=test_food_section_info)
    assert response.status_code == 201
    db_food_sections = list(db_utility.database.foodsections.find({}))
    assert len(db_food_sections) == 1
    assert test_food_section_info["name"] == db_food_sections[0]["name"]


@pytest.mark.tcid50
@pytest.mark.usefixtures("create_random_food_section")
def test_attempt_create_food_section_with_existing_name(client_is_staff_token, db_utility, random_food_section_info):
    existing_food_section = list(db_utility.foodsections.aggregate([{'$sample': {"size": 1}}]))
    random_food_section_info["name"] = existing_food_section[0]["name"]
    response = client_is_staff_token.post("api/food-section/create", json=random_food_section_info)
    assert response.status_code == 500
    db_food_sections = list(db_utility.database.foodsections.find({}))
    assert len(db_food_sections) == 1
    assert db_food_sections[0]["name"] == existing_food_section[0]["name"]


@pytest.mark.tcid51
@pytest.mark.usefixtures("create_random_food_section")
def test_attempt_create_food_section_with_existing_ordering_priority(
        client_is_staff_token, db_utility, random_food_section_info
):
    existing_food_section = list(db_utility.foodsections.aggregate([{'$sample': {"size": 1}}]))
    random_food_section_info["ordering_priority"] = existing_food_section[0]["ordering_priority"]
    response = client_is_staff_token.post("api/food-section/create", json=random_food_section_info)
    assert response.status_code == 500
    db_food_sections = list(db_utility.database.foodsections.find({}))
    assert len(db_food_sections) == 1
    assert db_food_sections[0]["ordering_priority"] == existing_food_section[0]["ordering_priority"]


@pytest.mark.tcid53
def test_attempt_create_food_section_with_empty_name(client_is_staff_token, db_utility, random_food_section_info):
    random_food_section_info["name"] = ''
    response = client_is_staff_token.post("api/food-section/create", json=random_food_section_info)
    assert response.status_code == 409
    db_food_sections = list(db_utility.database.foodsections.find({}))
    assert len(db_food_sections) == 0


@pytest.mark.tcid54
def test_attempt_create_food_section_with_empty_ordering_priority(
        client_is_staff_token, db_utility, random_food_section_info
):
    random_food_section_info["ordering_priority"] = ''
    response = client_is_staff_token.post("api/food-section/create", json=random_food_section_info)
    assert response.status_code == 409
    db_food_sections = list(db_utility.database.foodsections.find({}))
    assert len(db_food_sections) == 0


@pytest.mark.tcid55
def test_attempt_create_user_with_empty_image(client_is_staff_token, db_utility, random_food_section_info):
    random_food_section_info["image"] = ''
    response = client_is_staff_token.post("api/user/create", json=random_food_section_info)
    assert response.status_code == 409
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 1


@pytest.mark.tcid56
def test_attempt_create_user_with_empty_is_active(client_is_staff_token, db_utility, random_food_section_info):
    random_food_section_info["is_active"] = ''
    response = client_is_staff_token.post("api/user/create", json=random_food_section_info)
    assert response.status_code == 409
    db_users = list(db_utility.database.users.find({}))
    assert len(db_users) == 1
