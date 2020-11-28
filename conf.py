import json
from pathlib import Path


class Config:
    config_path = "conf/config.json"

    def __init__(self):
        self.config_json = {"connections": []}

    def init_config(self):
        conf_path = Path('conf')
        if not conf_path.is_dir():
            conf_path.mkdir()
        with open(self.config_path, "w+") as dump_f:
            json.dump(self.config_json, dump_f)

    def read_config(self):
        my_file = Path(self.config_path)
        if not my_file.is_file():
            self.init_config()

        with open(self.config_path, 'r') as load_f:
            self.config_json = json.load(load_f)

    def save_config(self):
        with open(self.config_path, "w") as dump_f:
            json.dump(self.config_json, dump_f)

    def get(self, path):
        return self.config_json[path]

    def set(self, path, json_obj):
        self.config_json[path] = json_obj

    def get_list_item(self, path, index):
        return self.config_json[path][index]

    def add_list_item(self, path, json_obj):
        if self.config_json[path] is None:
            self.config_json[path] = []
        self.config_json[path].append(json_obj)

    def del_list_item(self, path, index):
        if self.config_json[path] is None:
            self.config_json[path] = []
        del self.config_json[path][index]
