import json
from pathlib import Path

class Config():
    config_path = "conf/config.json"

    def init_config(self):
        self.config_json = {"connections": []}
        conf_path = Path('conf')
        if(conf_path.is_dir() == False):
            conf_path.mkdir()
        with open(self.config_path, "w+") as dump_f:
            json.dump(self.config_json, dump_f)

    def read_config(self):
        my_file = Path(self.config_path)
        if(my_file.is_file() == False):
            self.init_config()

        with open(self.config_path, 'r') as load_f:
            self.config_json = json.load(load_f)

    def save_config(self):
        with open(self.config_path, "w") as dump_f:
            json.dump(self.config_json, dump_f)

    def get(self, path):
        return self.config_json[path]

    def set(self, path, jsonObj):
        self.config_json[path] = jsonObj

    def add_list_item(self, path, jsonObj):
        if(self.config_json[path] == None):
            self.config_json[path] = []
        self.config_json[path].append(jsonObj)

