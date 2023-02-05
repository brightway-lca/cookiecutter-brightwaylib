"""Helper functions for the package.
"""
import importlib.metadata
from typing import Union


def get_version_tuple() -> tuple:
    """Get the package version as a tuple.

    Returns:
        tuple: the package version as a tuple following semantic versioning.
    """

    def as_integer(x: str) -> Union[int, str]:  # pylint: disable=C0103
        try:
            return int(x)
        except ValueError:
            return x

    return tuple(
        as_integer(v) for v in importlib.metadata.version("bw2ui").strip().split(".")
    )
