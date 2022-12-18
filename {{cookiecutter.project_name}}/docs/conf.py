"""Sphinx configuration."""
import importlib.metadata

project = "{{cookiecutter.project_name}}"
author = "{{cookiecutter.full_name}}"
copyright = "{{cookiecutter.copyright_year}}, {{cookiecutter.full_name}}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
{%- if cookiecutter.command_line_interface == 'Click' %}
    "sphinx_click",
{%- endif %}
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"

needs_sphinx = '5.0'

version = importlib.metadata.version("{{ cookiecutter.package_name }}")
