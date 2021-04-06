from dataclasses import dataclass
from typing import List, Dict, Tuple, Union, Optional

@dataclass
class Meal:
    name: str
    calories: float

@dataclass
class Location:
    city: str
    coords: Tuple[int,int]

@dataclass
class Person:
    name: str
    age: str
    meals: List[Meal]
    happy: bool
    location: Location
    optional_nickname: Optional[str]
