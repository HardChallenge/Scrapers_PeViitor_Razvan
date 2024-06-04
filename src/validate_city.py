from .county import counties, remove_diacritics
from .neighborhood import neighborhoods
from .county import misspelled_cities


def validate_city(city: str) -> str:
    # Check if the city is the name of a neighborhood
    city = remove_diacritics(city).lower()
    for item in neighborhoods.items():
        for value in item[1]:
            if city == remove_diacritics(value.lower()):
                return item[0]

    for item in misspelled_cities:
        for key, value in item.items():
            if city in value:
                return key

    for item in counties:
        for key, values in item.items():
            for value in values:
                if city == remove_diacritics(value.lower()):
                    return value
    return None
