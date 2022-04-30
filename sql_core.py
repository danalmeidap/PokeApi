from typing import List

import sqlalchemy
from sqlmodel import select

from database import get_session
from models import Pokedex


def add_pokemon_to_pokedex(
    name: str, weight: int, height: int, type: str, abilities: str
) -> bool:
    """Add pokemon to Pokedex database"""
    try:
        with get_session() as session:
            pokemon = Pokedex(**locals())
            session.add(pokemon)
            session.commit()
    except sqlalchemy.exc.IntegrityError:
        return False
    return True


def get_pokemons_from_database() -> List[Pokedex]:
    """List pokemons from Pokedex database"""
    with get_session() as session:
        sql = select(Pokedex)
        return list(session.exec(sql))


def get_pokemon_from_database_by_id(pokedex_id) -> List[Pokedex]:
    """Get a pokemon from Pokedex by id"""
    with get_session() as session:
        statement = select(Pokedex).where(Pokedex.id == pokedex_id)
        return list(session.exec(statement))


def delete_pokemon_from_database(pokedex_id: int) -> bool:
    """Dekete a pokemon from Pokedex by id"""
    with get_session() as session:
        statement = select(Pokedex).where(Pokedex.id == pokedex_id)
        results = session.exec(statement)
        employee = results.one()
        session.delete(employee)
        session.commit()
        return True
