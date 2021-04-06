from typing import List

from .utils import MealType, FlatPerson, PersonType

def extract_age(age_description:str)->int:
    """Extracts the age in number of years from a given age description string"""
    trimmed = age_description.replace(" years old", "").replace(" year old", "")
    return int(trimmed)


def extract_meal_names(meals:List[MealType])->List[str]:
    """Extracts the Meal names from a list of meals, this can be used for ..."""
    meal_names = set()
    for meal in meals:
        meal_names.add(meal["name"])
    return sorted(list(meal_names))

def extract_calorie_intake(meals:List[MealType])->float:
    """Extracts the total calories from a list of meals, this can be used for ..."""
    total_intake = 0
    for meal in meals:
        total_intake = total_intake + meal["calories"]
    return total_intake


def flatten_person(person:PersonType)->FlatPerson:
    """Flattens the data structure ready for conversion to csv"""
    return {
        "name": person["name"],
        "age": extract_age(person["age"]),
        "meals": ", ".join(extract_meal_names(person["meals"])),
        "calorie_intake": extract_calorie_intake(person["meals"]),
        "happy": person["happy"],
        "latitude": person["location"]["coords"][0],
        "longitude": person["location"]["coords"][1],
        "nickname": person.get("optional_nickname", ""),
    }

def flatten_people(people:List[PersonType])->List[FlatPerson]:
    """Flattens multiple person objects to make mutiple lines in the csv"""
    output = []
    for person in people:
        if person["happy"]:
            output.append(flatten_person(person))
    return output
