from itertools import product

class Phase3:
    def generate_combinations(self, lists, predefined_passwords, chunk_size=1000):
        """
        Génère des combinaisons à partir de listes d'entrée et teste si elles correspondent à des mots de passe prédéfinis.

        Args:
            lists (list of list): Les listes d'entrée pour générer des combinaisons.
            predefined_passwords (list): Les mots de passe prédéfinis à tester.
            chunk_size (int): La taille de chaque chunk de combinaisons à tester en une seule fois.

        Returns:
            list: Une liste de mots de passe trouvés parmi les combinaisons.

        """
        current_chunk = []
        found_passwords = []

        for combo in product(*lists):
            concatenated_combo = ''.join(map(str, combo))
            current_chunk.append(concatenated_combo)

            if len(current_chunk) >= chunk_size:
                found_passwords.extend(self.test_combinations(current_chunk, predefined_passwords))
                current_chunk = []

        if current_chunk:
            found_passwords.extend(self.test_combinations(current_chunk, predefined_passwords))

        return found_passwords

    def test_combinations(self, combinations, predefined_passwords):
        """
        Teste si les combinaisons correspondent à des mots de passe prédéfinis.

        Args:
            combinations (list): Les combinaisons à tester.
            predefined_passwords (list): Les mots de passe prédéfinis à comparer.

        Returns:
            list: Une liste des combinaisons qui correspondent aux mots de passe prédéfinis.

        """
        found_passwords = []

        for combo in combinations:
            if combo in predefined_passwords:
                found_passwords.append(combo)

        return found_passwords
