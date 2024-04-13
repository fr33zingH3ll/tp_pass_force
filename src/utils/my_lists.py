import string

INTEGERS = [i for i in range(10)]

SPECIALS = ["#", "_", "!", "-", "&", ";"]

ANIMAL = ["dauphin", "dragon"]

COLORS = ["Violet", "Jaune", "Indigo", "Orange", "Bleu", "Rouge", "Vert"]

LETTERS_LOWERCASE = list(string.ascii_lowercase)

LETTERS_UPPERCASE = list(string.ascii_uppercase)

ALLS = [INTEGERS, SPECIALS, ANIMAL, COLORS, LETTERS_LOWERCASE, LETTERS_UPPERCASE]

print(ALLS)