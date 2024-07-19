"""
3 Function, create_random_dictionary, write_dictionary_to_file, read_dictionary_from_file
Then main function to test the above functions
"""
import json
import random
from pathlib import Path


def create_random_dictionary(n:int) -> dict:
    """Create a dictionary with n random keys and values

    Args:
        n (int): Number of keys and values to generate

    Returns:
        dict: Random dictionary with n keys and values
    """    
    for i in range(n):
        random_dict = {random.randint(1, 100): random.randint(1, 100) for _ in range(n)}
    return random_dict

def write_dictionary_to_file(dictionary: dict, file_name: str):
    """Write dictionary to a file

    Args:
        dictionary (dict): Dictionary to write to file
        file_name (str): Name of the file to write to
    """    
    file_path = Path(file_name)
    if file_path.exists():
        print(f"File '{file_name}' already exists.")
        return
    
    with file_path.open('w') as file:
        json.dump(dictionary, file)

def read_dictionary_from_file(file_name: str) -> dict:
    """Read dictionary from a file

    Args:
        file_name (str): Name of the file to read from

    Returns:
        dict: Dictionary read from the file
    """    
    file_path = Path(file_name)
    if not file_path.exists():
        print(f"File '{file_name}' does not exist.")
        return
    
    with file_path.open() as file:
        dictionary = json.load(file)
    
    return dictionary

def main():
    random_dict = create_random_dictionary(5)
    print(f"Random dictionary: {random_dict}")

    file_name = 'random_dict.json'
    write_dictionary_to_file(random_dict, file_name)

    read_dict = read_dictionary_from_file(file_name)
    print(f"Read dictionary: {read_dict}")

if __name__ == '__main__':
    main()