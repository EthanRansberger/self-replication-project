import os
import json

def read_json(file_path):
    """
    Reads a JSON file and returns its content.
    :param file_path: Path to the JSON file.
    :return: Parsed JSON content as a dictionary.
    """
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json(data, file_path):
    """
    Writes a dictionary to a JSON file.
    :param data: Dictionary to write.
    :param file_path: Path to the JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def ensure_directory(directory):
    """
    Ensures that a directory exists.
    :param directory: Path to the directory.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

# Add more utility functions as needed
