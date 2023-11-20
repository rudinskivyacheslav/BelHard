# Дан словарь, ключ - Название страны, значение - список городов, на вход поступает город,
# необходимо сказать из какой он страны
globus = {"Belarus": ["Minsk", "Gomel", "Grodno"],
          "Usa": ["New York", "Houston", "Chicago", "Los Angeles"],
          "Poland": ["Varshava", "Krakov", "Wroclav"]}


def get_country(city_search: str):
    city_search = f"{city_search[0].upper()}{city_search[1:].lower()}"
    for counry, citys in globus.items():
        if city_search in citys:
            return counry
    return "No data"


print(get_country("GoMel"))
print(get_country("Osipovichi"))
print(get_country("Houston"))
