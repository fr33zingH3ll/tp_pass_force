from src.utils.database import MyDatabase
from src.utils.fields_options import IntegerOptions, TextOptions

class Phase1:
    def __init__(self, logger) -> None:
        self.db = MyDatabase("./src/resources/tp_pass_force.db", logger)
        self.db.create_table("Password", { 'id': IntegerOptions.integer_ai,'username': TextOptions.varchar, 'password': TextOptions.varchar })
        # self.db.insert_data("Password", 
        #                     [
        #                         (None, "Bob", "123456"),  # Laissez le champ "id" à None
        #                         (None, "Tom", "azerty"),
        #                         (None, "Tim", "marseille1993"),
        #                         (None, "Kay", "dauphinBleu"),
        #                         (None, "Zed", "dragon42"),
        #                         (None, "May", "naruto#7")
        #                     ])
        self.data = self.db.get_data("Password", ["password"])