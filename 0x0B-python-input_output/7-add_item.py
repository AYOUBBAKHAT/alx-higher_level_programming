#!/usr/bin/python3
'''task 7 module'''

import sys
from json import JSONDecodeError
from pathlib import Path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def main():
    arglist = list(sys.argv[1:])

    try:
        old_data = load_from_json_file('add_item.json')
    except FileNotFoundError:
        old_data = []
    except JSONDecodeError:
        print('Error: Unable to decode JSON from add_item.json')
        sys.exit(1)
    
    old_data.extend(arglist)

    try:
        save_to_json_file(old_data, 'add_item.json')
        print('Items added successfully.')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    main()
