from datetime import datetime

import pytest

pytestmark = pytest.mark.food_section_find


@pytest.mark.tcid68
@pytest.mark.usefixtures("create_test_food_section")
def test_attempt_food_section_find_with_random_token(client_random_token, db_utility):
    food_section_id = list(db_utility.foodsections.find({}))[0]["_id"]
    response = client_random_token.get(f"api/food-section/{food_section_id}/find")
    assert response.status_code == 405


@pytest.mark.tcid69
@pytest.mark.usefixtures("create_test_food_section")
def test_find_food_section(client_is_staff_token, test_food_section_info, db_utility):
    food_section_id = list(db_utility.foodsections.find({}))[0]["_id"]
    response = client_is_staff_token.get(f"api/food-section/{food_section_id}/find")
    assert response.status_code == 200
    db_food_sections = list(db_utility.foodsections.find({}))
    # Casting ObjectID to str for valid comparison
    db_food_sections[0]["_id"] = str(db_food_sections[0]["_id"])
    assert response.json()["item"] == db_food_sections[0]
