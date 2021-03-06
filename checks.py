from re import IGNORECASE, search
from typing import Match, Optional

import cli


def will_continue():
    check: bool = False
    while not check:
        answer: str = (
            str(input("Do you wanna search for another pokemon? [y/n]: "))
            .strip()
            .lower()
        )
        is_yes: Optional[Match[str]] = search("^y(es)?$", answer, IGNORECASE)
        is_no: Optional[Match[str]] = search("^n(o)?$", answer, IGNORECASE)
        if is_yes or is_no:
            if is_yes:
                cli.menu()
            else:
                check = confirm_no()
        else:
            print("Please, use only y(es) or n(o) for answer.")


def confirm_no() -> bool:
    answer: str = str(input("Are you sure? [y/n]: ")).strip().lower()
    is_yes: Optional[Match[str]] = search("^y(es)?$", answer, IGNORECASE)
    is_no: Optional[Match[str]] = search("^n(o)?$", answer, IGNORECASE)
    if is_yes or is_no:
        if is_yes:
            return True
        else:
            return False
    else:
        print("Please, use only y(es) or n(o) for answer.")


def will_save_in_pokedex() -> bool:
    check: bool = False
    while not check:
        answer: str = (
            str(input("Will you save pokemon in your pokedex? [y/n]: "))
            .strip()
            .lower()
        )
        is_yes: Optional[Match[str]] = search("^y(es)?$", answer, IGNORECASE)
        is_no: Optional[Match[str]] = search("^n(o)?$", answer, IGNORECASE)
        if is_yes or is_no:
            if is_yes:
                return True
            else:
                check = confirm_no()
        else:
            print("Please, use only y(es) or n(o) for answer.")
