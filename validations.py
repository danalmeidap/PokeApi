from sys import exit
from models import Pokemon
from reader import read_input_as_string, read_input_as_integer
from api import Api


def validate_pokemon(msg: str) -> Pokemon:
    while True:
        try:
            name: str = read_input_as_string(msg)
            if name.isalpha():
                verify: Pokemon = api.find_by_name(name)
                if verify:
                    return verify
            else:
                print("Invalid name for pokemon")
        except KeyboardInterrupt:
            exit("Interruptted by user")


def validate_id(msg: str) -> Pokemon:
    while True:
        try:
            poke_id: int = read_input_as_integer(msg)
            verify: Pokemon = api.find_by_id(poke_id)
            if verify:
                return verify
            else:
                print("Id is nos valid")
        except(ValueError, TypeError):
            print("The value should be an integer")
        except KeyboardInterrupt:
            exit("Interruptted by user")


def validate_option(msg: str) -> int:
    while True:
        try:
            value: int = read_input_as_integer(msg)
            if value > 0:
                return value
            else:
                print("The value must be positive and in the menu options")
        except(ValueError, TypeError):
            print("The value should be an integer")
        except KeyboardInterrupt:
            exit("Interruptted by user")


api = Api()
