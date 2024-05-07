from county import counties

misspelled_cities = [
    {"Bucuresti": ["bucharest", "bucuresti", "buharest", "buacharest", "buahcharest"]},
    {"Cluj-Napoca": ["cluj napoca", "cluj", "cluj-napoca"]},
    {"Bolintin-Deal": ["bolintin-deal", "bolintin - deal"]},
    {"Campulung": ["campulung muscel", "campulung Muscel"]},
    {"Poiana Lacului": ["poiana lacului"]},
]


def validate_city(city):
    for item in misspelled_cities:
        for key, value in item.items():
            if city.lower() in value:
                return key

    for item in counties:
        for key, values in item.items():
            for value in values:
                if city.lower() == value.lower():
                    return city
    return None
