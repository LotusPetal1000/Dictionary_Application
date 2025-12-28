import json
import os

def save_dict(file_name: str, dict_name: dict):
    with open(file_name, "w", encoding = "utf-8") as f:
        json.dump(dict_name, f, ensure_ascii= False, indent= 4)

def load_dict(file_name: str):
    if not os.path.exists(file_name):
        return {}
    with open(file_name, "r", encoding = "utf-8") as f:
        return json.load(f)

def create_dict(file_name: str):
    with open(file_name, "x") as f:
        return
