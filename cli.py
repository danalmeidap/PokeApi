from time import sleep
from typing import List

from rich import print
from rich.console import Console
from rich.table import Table

from core import search_for_id, search_for_name
from models import Pokedex
from sql_core import (
    delete_pokemon_from_database,
    get_pokemon_from_database_by_id,
    get_pokemons_from_database,
)
from validations import validate_option, validate_pokedex_index


def pokedex_list() -> None:
    """List employees from database"""
    pokemons: List[Pokedex] = get_pokemons_from_database()
    if len(pokemons) > 0:
        table = generate_pokedex_table(pokemons)
        console.print(table)
    else:
        print("Pokedex is empty")
    sleep(2)
    menu()


def search_on_pokedex_by_id():
    pokemons: List[Pokedex] = get_pokemons_from_database()
    if len(pokemons) > 0:
        pokedex_id: int = validate_pokedex_index("Index for searching: ")
        pokemon: List[Pokedex] = get_pokemon_from_database_by_id(pokedex_id)
        table: Table = generate_pokedex_table(pokemon)
        console.print(table)
    else:
        print("Pokedex is empty")
    sleep(2)
    menu()


def generate_pokedex_table(pokemons: List[Pokedex]) -> Table:
    table: Table = Table(title="Pokedex Database")
    headers: List[str] = [
        "id",
        "name",
        "weight",
        "height",
        "type",
        "abilities",
        "added_in",
    ]
    for header in headers:
        table.add_column(header, style="magenta")
    for poke in pokemons:
        poke.added_in = poke.added_in.strftime("%Y-%m-%d")
        values: List[str] = [str(getattr(poke, header)) for header in headers]
        table.add_row(*values)
    return table


def delete_on_pokedex_by_id():
    """Delete employee from database"""
    pokemons: List[Pokedex] = get_pokemons_from_database()
    if len(pokemons) > 0:
        pokedex_id: int = validate_pokedex_index("Index for searching: ")
        if delete_pokemon_from_database(pokedex_id):
            print("The pokemon was deleted")
        else:
            print("Operation not concluded")
    else:
        print("Pokedex is empty")
    sleep(2)
    menu()


def menu() -> None:
    print("Pokedex menu: ")
    print("1 - Search using pokemon's name")
    print("2 - Search using pokemon's id")
    print("3-  List Pokemons in your pokedex")
    print("4-  Search on pokedex by id")
    print("5 - Delete from pokedex by id")
    print("6 - Quit pokedex")

    option: int = validate_option("Option: ")

    if option == 1:
        search_for_name()
    if option == 2:
        search_for_id()
    if option == 3:
        pokedex_list()
    if option == 4:
        search_on_pokedex_by_id()
    if option == 5:
        delete_on_pokedex_by_id()
    if option == 6:
        print("See ya!")
        sleep(2)
        exit(0)
    else:
        print("Invalid Option")
        menu()


console = Console()
