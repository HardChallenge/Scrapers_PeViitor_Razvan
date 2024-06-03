from .county import counties, remove_diacritics
from .neighborhood import neighborhoods

misspelled_cities = [
    {
        "București": [
            "bucharest",
            "bucuresti",
            "buharest",
            "buacharest",
            "buahcharest",
            "buchares",
        ]
    },
    {"Cluj-Napoca": ["cluj napoca", "cluj", "cluj-napoca"]},
    {"Bolintin-Deal": ["bolintin-deal", "bolintin - deal"]},
    {"Câmpulung": ["campulung muscel", "campulung Muscel"]},
    {"Poiana Lacului": ["poiana lacului"]},
]


def validate_city(city: str) -> str:
    # Check if the city is the name of a neighborhood
    for item in neighborhoods.items():
        for value in item[1]:
            if city.lower() == remove_diacritics(value.lower()):
                return item[0]

    for item in misspelled_cities:
        for key, value in item.items():
            if city.lower() in value:
                return key

    for item in counties:
        for key, values in item.items():
            for value in values:
                if city.lower() == remove_diacritics(value.lower()):
                    return value
    return None
