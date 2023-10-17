from src.utils.database import MyDatabase
from src.utils.fields_options import IntegerOptions, TextOptions
from src.phase import Phase

class Phase1(Phase):
    def __init__(self) -> None:
        try:
            self.db = MyDatabase(db_file="src/resources/tp_pass_force.db")
            self.db.create_table("Password", { 'id': IntegerOptions.integer_ai,'username': TextOptions.varchar, 'password': TextOptions.varchar })
            self.db.insert_data("password", 
                                [
                                    ("Bob", "123456"),
                                    ("Tom", "azerty"),
                                    ("Tim", "marseille1993"),
                                    ("Kay", "dauphinBleu"),
                                    ("Zed", "dragon42"),
                                    ("May", "naruto#7")
                                ])
            self.finish()
        except Exception as e:
            self.error(e)