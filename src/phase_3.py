from itertools import product
from src.utils.my_lists import LAMBDA_ALGOS

def test_combinations(combinations, predefined_passwords, hash=None):
    """
    Teste si les combinaisons correspondent à des mots de passe prédéfinis.

    Args:
        combinations (list): Les combinaisons à tester.
        predefined_passwords (list): Les mots de passe prédéfinis à comparer.
        hash (str): L'algorithme de hachage à utiliser.

    Returns:
        list: Une liste des combinaisons qui correspondent aux mots de passe prédéfinis.

    """
    found_passwords = []

    for combo in combinations:
        if hash:
            hashed_combo = LAMBDA_ALGOS[hash](combo)
            if hashed_combo in predefined_passwords:
                found_passwords.append(hashed_combo)
        else:
            if combo in predefined_passwords:
                found_passwords.append(combo)

        print(combo)

    return found_passwords

def generate_combinations(lists, predefined_passwords, hash=None, chunk_size=1000):
    """
    Génère des combinaisons à partir de listes d'entrée et teste si elles correspondent à des mots de passe prédéfinis.

    Args:
        lists (list of list): Les listes d'entrée pour générer des combinaisons.
        predefined_passwords (list): Les mots de passe prédéfinis à tester.
        hash (str): L'algorithme de hachage à utiliser.
        chunk_size (int): La taille de chaque chunk de combinaisons à tester en une seule fois.

    Returns:
        list: Une liste de mots de passe trouvés parmi les combinaisons.

    """
    if len(predefined_passwords) == 0:
        return []
    
    liste_plate = [element for sous_liste in lists for element in sous_liste]
    iteration = 0
    concatenated_combo = ""

    found_passwords = []

    current_chunk = []

    # Boucler jusqu'à ce que tous les mots de passe soient trouvés
    while True:
        iteration += 1
        print(f"itération {iteration}")
        for i in range(iteration):
            for combo in liste_plate:
                concatenated_combo += ''.join(map(str, str(combo)))
            current_chunk.append(concatenated_combo)

            # Tester les combinaisons actuelles
            found_passwords.extend(test_combinations(current_chunk, predefined_passwords, hash=hash))

            # Si tous les mots de passe ont été trouvés, sortir de la boucle
            if set(found_passwords) == set(predefined_passwords):
                return found_passwords

        # Réinitialiser le chunk actuel
        current_chunk = []

        # Arrêter la boucle si la longueur de la liste dépasse le nombre de caractères dans l'alphabet
        if len(lists) > len(predefined_passwords):
            break

    return found_passwords


arguments = []