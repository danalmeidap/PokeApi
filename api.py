import json

import requests

from config import settings
from models import Pokemon


def fetch_data(json_file) -> Pokemon:
    return Pokemon(
        json_file["name"],
        json_file["id"],
        json_file["weight"],
        json_file["height"],
        " ".join(map(lambda x: x["type"]["name"], json_file["types"])),
        " ".join(map(lambda x: x["ability"]["name"], json_file["abilities"])),
    )


class Api:
    def __init__(self):
        self.__api = settings.api.url

    def find_by_name(self, name: str) -> Pokemon:
        data = requests.get(f"{self.__api}{name}")
        all_data = json.loads(data.content)
        return fetch_data(all_data)

    def find_by_id(self, pokemon_id: int) -> Pokemon:
        data = requests.get(f"{self.__api}{pokemon_id}")
        all_data = json.loads(data.content)
        return fetch_data(all_data)
