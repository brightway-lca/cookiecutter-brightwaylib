from pathlib import Path
from typing import Union


def get_version() -> tuple:
    def as_integer(x: str) -> Union[int, str]:
        try:
            return int(x)
        except ValueError:
            return x

    return tuple(
        as_integer(v)
        for v in open(Path(__file__).parent / "VERSION").read().strip().split(".")
    )


__version__ = get_version()
