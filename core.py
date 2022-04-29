from time import sleep

from checks import will_continue, will_save_in_pokedex
from models import Pokemon
from sql_core import add_pokemon_to_pokedex
from validations import validate_id, validate_pokemon


def search_for_name() -> None:
    pokemon: Pokemon = validate_pokemon("Please insert the pokemon name: ")
    print(pokemon)
    sleep(2)
    if will_save_in_pokedex():
        if add_pokemon_to_pokedex(
            pokemon.name,
            pokemon.weight,
            pokemon.height,
            pokemon.type,
            pokemon.abilities,
        ):
            print("Pokemon added")
        else:
            print("Pokemon is already in pokedex")
        will_continue()
    else:
        will_continue()
    print("See ya!")
    sleep(2)
    exit(0)


def search_for_id() -> None:
    pokemon: Pokemon = validate_id("Please insert the pokemon id: ")
    print(pokemon)
    sleep(2)
    if will_save_in_pokedex():
        if add_pokemon_to_pokedex(
            pokemon.name,
            pokemon.weight,
            pokemon.height,
            pokemon.type,
            pokemon.abilities,
        ):
            print("Pokemon added")
        else:
            print("Pokemon is already in pokedex")
        will_continue()
    else:
        will_continue()
    print("See ya!")
    sleep(2)
    exit(0)
