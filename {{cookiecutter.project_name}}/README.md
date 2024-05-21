# {{ cookiecutter.project_name }}

[![PyPI](https://img.shields.io/pypi/v/{{cookiecutter.project_name}}.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/{{cookiecutter.project_name}}.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/{{cookiecutter.project_name}})][pypi status]
[![License](https://img.shields.io/pypi/l/{{cookiecutter.project_name}})][license]

[![Read the documentation at https://{{cookiecutter.project_name}}.readthedocs.io/](https://img.shields.io/readthedocs/{{cookiecutter.project_name}}/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/actions/workflows/python-test.yml/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi status]: https://pypi.org/project/{{cookiecutter.project_name}}/
[read the docs]: https://{{cookiecutter.project_name}}.readthedocs.io/
[tests]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Installation

You can install _{{cookiecutter.package_name}}_ via [pip] from [PyPI]:

```console
$ pip install {{cookiecutter.package_name}}
```

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide][Contributor Guide].

## License

Distributed under the terms of the [{{cookiecutter.open_source_license.replace("-", " ")}} license][License],
_{{cookiecutter.package_name}}_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue][Issue Tracker] along with a detailed description.


<!-- github-only -->

[command-line reference]: https://{{cookiecutter.project_name}}.readthedocs.io/en/latest/usage.html
[License]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/blob/main/LICENSE
[Contributor Guide]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/blob/main/CONTRIBUTING.md
[Issue Tracker]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/issues


## Building the Documentation

You can build the documentation locally by installing the documentation Conda environment:

```bash
conda env create -f docs/environment.yml
```

activating the environment

```bash
conda activate sphinx_{{cookiecutter.project_name}}
```

and [running the build command](https://www.sphinx-doc.org/en/master/man/sphinx-build.html#sphinx-build):

```bash
sphinx-build docs _build/html --builder=html --jobs=auto --write-all; open _build/html/index.html
```