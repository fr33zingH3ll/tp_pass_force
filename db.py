import sqlite3


class DB:

    PATH = "./src/"
    db_name = "tp_pass_force"

    def __init__(self) -> None:
        self.con = sqlite3.connect(f"{self.PATH}{self.db_name}.db")
        self.cur = self.con.cursor()

    def create_table(self, table_name, list_champs, debug = False):
        injection = ""
        for index, champ in enumerate(list_champs):
            if index != len(list_champs) - 1:
                injection += champ + ","
            else:
                injection += champ
        self.execute(f"CREATE TABLE IF NOT EXISTS {table_name}({injection})", debug)

    def insert(self, table_name, dict_values, debug = False):
        champs = ""
        values = ""
        for index, item in enumerate(dict_values['champs']):
            if index != len(dict_values['champs']) - 1:
                champs += item + ","
            else:
                champs += item
        for index, item in enumerate(dict_values['values']):
            if index != len(dict_values['values']) - 1:
                values += f"('{item[0]}','{item[1]}'),"
            else:
                values += f"('{item[0]}','{item[1]}')"
        self.execute(f"INSERT INTO {table_name}({champs}) VALUES {values}", debug)

    def get_all(self, table_name, debug = False):
        item_list = []
        res = self.execute(f"SELECT * FROM {table_name}", debug)
        fetch = res.fetchall()
        for item in fetch:
            item_list.append(list(item))
        return item_list

    def execute(self, req, debug):
        if debug : print(req)
        res = self.cur.execute(req)
        return res
    