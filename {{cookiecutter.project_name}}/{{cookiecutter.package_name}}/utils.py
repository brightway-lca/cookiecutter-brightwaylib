"""Utilities module for {{cookiecutter.package_name}}."""
import importlib.metadata
from typing import Union


def get_version_tuple() -> tuple:
    """Returns version as (major, minor, micro)."""

    def as_integer(version_str: str) -> Union[int, str]:
        try:
            return int(version_str)
        except ValueError:
            return version_str

    return tuple(
        as_integer(v)
        for v in importlib.metadata.version("{{ cookiecutter.package_name }}")
        .strip()
        .split(".")
    )
