# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение - словарь с данными
# о пользователе (имя, фамилия, телефон, почта), вывести имена тех, у кого не указана почта
# (нет ключа email или значение этого ключа - пустая строка)
dictionary = {
    43935430: {"name": "Alex", "last_name": "Rumanov", "phone_number": 3469847293, "email": "alex@gmail.com"},
    43983450: {"name": "Blaid", "last_name": "Pugach", "phone_number": 3469847293, "email": ""},
    43345450: {"name": "Pit", "last_name": "Kaluzi", "phone_number": 3469847293, "email": "alex@gmail.com"},
    44833460: {"name": "Fil", "last_name": "Rudi", "phone_number": 3469847293, "email": None},
              }
for user in filter(lambda u: u.get("email"), dictionary.values()):
    print(user.get("name"))
