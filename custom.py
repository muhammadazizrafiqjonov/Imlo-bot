from transliterate import to_latin
from uzwords import words


# Kirill so'zlardan iborat list
kirill_sozlar = words

# Kirill so'zlarni lotinga o'zgartirish
latin_sozlar = [to_latin(soz) for soz in kirill_sozlar]

# Natijani alohida Python faylga yozish
with open("latin_sozlar.py", "w", encoding="utf-8") as file:
    file.write("# Lotin so'zlar listi\n")
    file.write(f"latin_sozlar = {latin_sozlar}\n\n")