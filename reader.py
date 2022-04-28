def read_input_as_string(msg) -> str:
    a_string: str = str(input(msg)).strip().lower()
    return a_string


def read_input_as_integer(msg) -> int:
    an_integer: int = int(input(msg))
    return an_integer
