from src.utils.database import MyDatabase
from src.utils.fields_options import IntegerOptions, TextOptions


class Phase1:
    def __init__(self) -> None:
        self.db = MyDatabase(db_file="src/resources/tp_pass_force.db")
        self.db.create_table("Password", { 'id': IntegerOptions.integer_ai,'username': TextOptions.varchar, 'password': TextOptions.varchar })
        self.db.insert_data("Password", 
                            [
                                ("Bob", "123456"),
                                ("Tom", "azerty"),
                                ("Tim", "marseille1993"),
                                ("Kay", "dauphinBleu"),
                                ("Zed", "dragon42"),
                                ("May", "naruto#7")
                            ])