"""Sphinx configuration."""
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
