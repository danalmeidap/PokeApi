from validations import validate_option
from time import sleep
from core import search_for_name, search_for_id


def menu() -> None:
    print('Pokedex menu: ')
    print("1 - Search using pokemon's name")
    print("2 - Search using pokemon's id")
    print('3 - Quit pokedex')

    option: int = validate_option("Option: ")

    if option == 1:
        search_for_name()
    if option == 2:
        search_for_id()
    if option == 3:
        print("See ya!")
        sleep(2)
        exit(0)
    else:
        print("Invalid Option")
        menu()