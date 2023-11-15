#Код Морзе для представления цифр и букв использует тире и точки. Напишите функцию для кодирования
# текстового сообщения в соответствии с кодом Морзе. (словари в помощь)
morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••', 'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—', 'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
         '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}


def convert_to_morse(line: str):
    result = ""
    for ch in line.lower():
        if ch in morze:
            result = f"{result}{morze.get(ch)}"

    return result


print(convert_to_morse("Hello Python"))
