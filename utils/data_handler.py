import json
import os

def load_config():
    """Reads and parses the base system configuration variables from config/config.json"""
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../config/config.json"))
    with open(config_path, "r") as config_file:
        return json.load(config_file)

def load_test_data():
    """Reads and parses the user testing credentials from config/test_data.json"""
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../config/test_data.json"))
    with open(data_path, "r") as data_file:
        return json.load(data_file)
