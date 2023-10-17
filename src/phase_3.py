from src.utils.logs_manager import logger

class Phase3:
    complement = [
        "Violet","Jaune","Indigo",
        "Orange","Bleu","Rouge","Vert"
    ]
    def combine_lists(self, list1):
        return [item1 + item2 for item1 in list1 for item2 in self.complement]

    def add_ids_to_list(input_list):
        return [f"{item}{str(i).zfill(4)}" for i, item in enumerate(input_list)]

    def find_common_elements(self, list1, list2):
        return [item for item in list1 if item in list2]