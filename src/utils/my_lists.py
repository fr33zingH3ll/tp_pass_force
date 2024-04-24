import string
import hashlib

INTEGERS = [i for i in range(10)]

SPECIALS = ["#", "_", "!", "-", "&", ";"]

ANIMAL = ["dauphin", "dragon"]

COLORS = ["Violet", "Jaune", "Indigo", "Orange", "Bleu", "Rouge", "Vert"]

LETTERS_LOWERCASE = list(string.ascii_lowercase)

LETTERS_UPPERCASE = list(string.ascii_uppercase)

LAMBDA_ALGOS = {          
    "MD5": lambda password: hashlib.md5(password.encode("utf-8")).hexdigest(),
    "SHA1": lambda password: hashlib.sha1(password.encode("utf-8")).hexdigest(),
    "SHA224": lambda password: hashlib.sha224(password.encode("utf-8")).hexdigest(),
    "SHA256": lambda password: hashlib.sha256(password.encode("utf-8")).hexdigest(),
    "SHA384": lambda password: hashlib.sha384(password.encode("utf-8")).hexdigest(),
    "SHA512": lambda password: hashlib.sha512(password.encode("utf-8")).hexdigest(),
}

ALGOS = list(LAMBDA_ALGOS.keys())
ALGOS.insert(0, "")

ALLS = {"INTEGERS": INTEGERS, "SPECIALS": SPECIALS, "ANIMAL": ANIMAL, "COLORS": COLORS, "LETTERS_LOWERCASE": LETTERS_LOWERCASE, "LETTERS_UPPERCASE": LETTERS_UPPERCASE, "ALGOS": ALGOS}

print(ALLS)