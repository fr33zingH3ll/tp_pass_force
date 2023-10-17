from itertools import product

class Phase3:
    def generate_combinations(self, lists, predefined_passwords, chunk_size=1000):
        current_chunk = []
        found_passwords = []

        for combo in product(*lists):
            concatenated_combo = ''.join(map(str, combo))
            current_chunk.append(concatenated_combo)

            if len(current_chunk) >= chunk_size:
                found_passwords.extend(self.test_combinations(current_chunk, predefined_passwords))
                current_chunk = []

        # Assurez-vous de renvoyer la dernière partie, si elle n'est pas vide
        if current_chunk:
            found_passwords.extend(self.test_combinations(current_chunk, predefined_passwords))

        return found_passwords

    def test_combinations(self, combinations, predefined_passwords):
        found_passwords = []

        for combo in combinations:
            if combo in predefined_passwords:
                found_passwords.append(combo)

        return found_passwords
    