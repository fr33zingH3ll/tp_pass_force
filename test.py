from itertools import product
import string
from src.utils.my_lists import LAMBDA_ALGOS

text = "e476d146af22c5a790966cde9600f8daa78bbaee1482581561d2c76389a2f125"
integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
lists = [integers, lowercase]
liste_plate = [element for sous_liste in lists for element in sous_liste]
iteration = 0

game = True

while game:  # Changez 3 par le nombre d'itérations souhaité
    iteration += 1
    print(iteration)
    for combination in product(liste_plate, repeat=iteration):
        password = ''.join(map(str, combination))
        if LAMBDA_ALGOS["SHA256"](password) == text:
            print(password)
            game = False