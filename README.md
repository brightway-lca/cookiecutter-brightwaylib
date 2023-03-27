# cookiecutter-brightwaylib

A [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/index.html) based project template for Brightway ecosystem packages.

# [Usage](https://cookiecutter.readthedocs.io/en/stable/usage.html)

## Installation

1. Create a new environment (pip or conda), activate it, and install `cookiecutter`
2. Download (i.e. don't install via pip or conda) this repository, either directly or via git
3. Edit the `cookiecutter.json` file to give your personal info. You should update at least:

* "full_name"
* "email"
* "project_name". This will be the github repo and pypi name. Should not include dashes or spaces.
* "github_username" if not intended for submission to `https://github.com/brightway-lca/`

## Creating a new package

1. Invoke cookiecutter *in the parent directory of `cookiecutter-brightwaylib`*

```
cookiecutter cookiecutter-brightwaylib/
```

You will need to answer questions regarding:

+ A one-sentence project description
+ Version string (default 0.1.0)
+ Whether or not you want to use [click](https://click.palletsprojects.com/en/8.1.x/) for CLI (default yes)
+ Which license to use (default MIT)

## Uploading your package

1. Install `build` and `twine` in your current or a new environment
2. Configure `twine` with you [pypi username and password](https://twine.readthedocs.io/en/stable/#configuration) with your [pypi API token](https://pypi.org/help/#apitoken).
3. Run `python -m build` 
4. Run `twine upload dist/*`

You can also consider [uploading to testpypi](https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives) first.

# Features

+ github actions:
    + test `main` and `develop` on push and on pull requests to this branches on the following:
        + os: [ubuntu-latest, windows-latest, macos-latest]
        + py-version: ["3.8", "3.9", "3.10", "3.11"]
    + build source and wheel distribution packages using [build as backend](https://packaging.python.org/en/latest/key_projects/#build)
    + upload to `test.pypi.org` on push events to the `develop` branch
    + upload to `pypi.org` on tagged push events to the `main` branch whose tag starts with **the letter `v`**, e.g. `v1.0`. The version **does not** depend on the tag, it is taken from the `VERSION` file.
+ pytest
+ source folder is at the root of the project, and **not** under `src` !
+ `pyproject.toml` used for **configuring the build system only**
+ `setup.cfg` contains the configuration of the package (name, install_requires, metadata)

# Requirements

## pre-commit

Follow the instructions at the [pre-commit website](https://pre-commit.com/).

In our pre-commit configuration, we run pylint, and this needs to be installed locally as its Github repo doesn't play nicely with pre-commit.

## Secrets for publishing
The github actions to publish to test.pypi.org and pypi.org require the creation of the following 2 secrets:

+ `TEST_PYPI_API_TOKEN`
+ `PYPI_API_TOKEN`

No username is necessary because the github action uses the new `__token__` based approach.
The previous secrets are the tokens generated through the test.pypi.org and pypi.org sites.
See [uploading distribution archives](https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives) for more information.
