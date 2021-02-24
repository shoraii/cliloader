#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import colorama
from colorama import Fore, Back, Style
import json
import os.path
import requests
import string


def main(path_to_file):
    if not os.path.exists(path_to_file):
        print(f'File {path_to_file} does not exist!')
        return
    if os.path.getsize(path_to_file) > 50 * 1000 * 1000:
        print(f'File {path_to_file} has size more than 50KB!')
        return
    with open(path_to_file, 'rb') as f:
        print(f'Uploading {path_to_file}...')
        response = requests.post('https://uploadir.com/uploads.json', files= {'upload[file][]' : f.read()})
        if response.status_code == 201:
            print(Style.BRIGHT + Fore.GREEN + f'Uploaded {path_to_file} successfully!')
            url = response.json()[0]['download']
            delete = response.json()[0]['delete']
            print(Fore.CYAN + f'Link to the file: https://uploadir.com/u/{url}')
            print(Fore.RED + f'Link to the deletion: https://uploadir.com/d/{url}//{delete}')
        else:
            print(Fore.RED + f'Couldn\'t upload the file, status code: {response.status_code}!')


if __name__ == '__main__':
    colorama.init(autoreset=True)
    parser = argparse.ArgumentParser(description='cliloader: upload small files to uploadir.com via terminal')
    parser.add_argument(
        'path_to_file',
        action='store',
        help='path to file')
    args = parser.parse_args()
    main(args.path_to_file)