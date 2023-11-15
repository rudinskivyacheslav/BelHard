# Дан словарь, ключ - Название страны, значение - список городов, на вход поступает город,
# необходимо сказать из какой он страны
globus = {"Belarus": ["Minsk", "Gomel", "Grodno"], "Usa": ["New York", "Houston", "Chicago", "Los Angeles"],
          "Poland": ["Varshava", "Krakov", "Wroclav"]}


def get_country(city_search: str):
    for counry, citys in globus.items():
        for city in citys:
            if city_search.lower() == city.lower():
                return counry
    else:
        return "No data"


print(get_country("miNSK"))
print(get_country("Osipovichi"))
print(get_country("Houston"))
