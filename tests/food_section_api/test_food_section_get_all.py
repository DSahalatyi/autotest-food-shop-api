import pytest

pytestmark = pytest.mark.food_section_get_all


@pytest.mark.tcid66
@pytest.mark.usefixtures("create_random_food_section")
def test_get_all_food_sections(client_is_staff_token, random_food_section_info, db_utility):
    response = client_is_staff_token.get("api/food-section/get-all")
    assert response.status_code == 200
    db_food_sections = list(db_utility.foodsections.find({}))
    assert len(db_food_sections) == 1
    assert db_food_sections[0]["name"] == random_food_section_info["name"]
    assert db_food_sections[0]["ordering_priority"] == random_food_section_info["ordering_priority"]
    assert db_food_sections[0]["is_available"] == random_food_section_info["is_available"]


@pytest.mark.tcid67
@pytest.mark.usefixtures("db_utility")
def test_attempt_get_all_food_sections_with_random_token(client_random_token):
    response = client_random_token.get("api/food-section/get-all")
    assert response.status_code == 405
