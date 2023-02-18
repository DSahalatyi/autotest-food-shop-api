import pytest


pytestmark = pytest.mark.food_section_delete


@pytest.mark.tcid70
@pytest.mark.usefixtures("create_test_food_section")
def test_attempt_delete_food_section_with_random_token(client_random_token, db_utility):
    food_section_id = list(db_utility.foodsections.find({}))[0]["_id"]
    response = client_random_token.get(f"api/food-section/{food_section_id}/delete")
    assert response.status_code == 405
    db_food_sections = list(db_utility.foodsections.find({}))
    assert len(db_food_sections) == 1


@pytest.mark.tcid71
@pytest.mark.usefixtures("create_test_food_section")
@pytest.mark.usefixtures("create_random_food_section")
def test_delete_food_section(client_is_staff_token, test_food_section_info, db_utility):
    food_section_id = list(db_utility.foodsections.find({}))[0]["_id"]
    response = client_is_staff_token.get(f"api/food-section/{food_section_id}/delete")
    assert response.status_code == 200
    db_food_sections = list(db_utility.foodsections.find({}))
    assert len(db_food_sections) == 1
    assert db_food_sections[0]["name"] == test_food_section_info["name"]
    