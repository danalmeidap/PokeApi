from time import sleep

from checks import will_continue
from models import Pokemon
from validations import validate_id, validate_pokemon


def search_for_name() -> None:
    pokemon: Pokemon = validate_pokemon("Please insert the pokemon name: ")
    print(pokemon)
    sleep(2)
    will_continue()
    print("See ya!")
    sleep(2)
    exit(0)


def search_for_id() -> None:
    pokemon: Pokemon = validate_id("Please insert the pokemon id: ")
    print(pokemon)
    sleep(2)
    will_continue()
    print("See ya!")
    sleep(2)
    exit(0)
