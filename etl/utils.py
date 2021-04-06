from typing import List, Dict, Tuple, Union, Optional

MealType = Dict[str, Union[str, float]]
LocationType = Dict[str, Union[str, Tuple[int,int]]]
PersonType = Dict[str, Union[str, List[MealType], bool, LocationType]]
FlatPerson = Dict[str, Union[str, float, bool]]