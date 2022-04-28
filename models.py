class Pokemon:
    def __init__(self, name: str, pokemon_id: int, pokemon_weight: int, pokemon_height: int, pokemon_type: str,
                 pokemon_abilities: str) -> None:
        self.__name: str = name
        self.__id: int = pokemon_id
        self.__weight: int = pokemon_weight
        self.__height: int = pokemon_height
        self.__type: str = pokemon_type
        self.__abilities: str = pokemon_abilities

    @property
    def name(self) -> str:
        return self.__name

    @property
    def id(self) -> int:
        return self.__id

    @property
    def weight(self) -> int:
        return self.__weight

    @property
    def height(self) -> int:
        return self.__height

    @property
    def type(self) -> str:
        return self.__type

    @property
    def abilities(self) -> str:
        return self.__abilities

    def __repr__(self) -> str:
        representation: str = ""
        representation += f"Id: {self.__id}" + "\n"
        representation += f"Name: {self.__name}" + "\n"
        representation += f"Weight: {self.__weight}" + "\n"
        representation += f"Height: {self.__height}" + "\n"
        representation += f"Type: {self.__type}" + "\n"
        representation += f"Abilities: {self.__abilities}"
        return representation

    def __str__(self: object) -> str:
        return self.__repr__()
