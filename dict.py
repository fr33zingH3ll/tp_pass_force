import requests

class Dict:
    dict_common_pass = {}
    FOLDER_PATH = "./src/"

    def __init__(self, list) -> None:
        self.dict_common_pass = self.get_common_pass(list)
        self.save_dict_common_pass()
        self.list_code_XXXX()
    def get_common_pass(self, list):
        temp_dict = {}
        for i in list:
            temp_dict[i] = requests.get(f"https://nordpass.com/json-data/top-worst-passwords/findings/{i}.json").json()
        return temp_dict
    
    def save_dict_common_pass(self):
        for key, value in self.dict_common_pass.items():
            with open(f"{self.FOLDER_PATH}dictionnaire_{key}.txt", "w") as file:
                for password in value:
                    file.write(str(password['Password'])+"\n")
    
    def list_code_XXXX(self):
        with open(f"{self.FOLDER_PATH}number.txt", "w") as file:
            for a in range(10):
                for b in range(10):
                    for c in range(10):
                        for d in range(10):
                            file.write(str(a) + str(b) + str(c) + str(d) + "\n")