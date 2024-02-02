# cookiecutter-brightwaylib

A [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/index.html) based project template for Brightway ecosystem packages.

We prefer using `cruft` as tooling to create/check/update projects created with the template over direct cookiecutter because of the following features of [cruft](https://cruft.github.io/cruft/):

+ it is actively maintained
+ it allows to check if the project is up to date with the template
+ it allows to update the project, based on changes on the template

# [Usage](https://cruft.github.io/cruft/)

## Installation

1. Create a new environment (pip, conda, mamba, choose your 💊),
2. Activate the newly created envionrment and install `cruft` ( `mamba install cruft` for example)
3. Create a project with:

```
cruft create https://github.com/brightway-lca/cookiecutter-brightwaylib
```

You will be asked for the following information:
* "full_name"
* "email"
* "project_name". This will be the github repo and pypi name. Should not include dashes or spaces.
* "github_username" if not intended for submission to `https://github.com/brightway-lca/`
+ A one-sentence project description
+ Version string (default 0.0.1)
+ Which license to use (default MIT)

## Updating the project

If the cookiecutter template is updated, you can upgrade your project with:

```
cruft update
```
inside the repository of the project. See [cruft documentation](https://cruft.github.io/cruft/#updating-a-project) for more on this.

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
        + py-version: ["3.9", "3.10", "3.11", "3.12"]
    + build source and wheel distribution packages using [build as backend](https://packaging.python.org/en/latest/key_projects/#build)
    + upload to `test.pypi.org` on push events to the `develop` branch
    + upload to `pypi.org` on tagged push events to the `main` branch whose tag starts with **the letter `v`**, e.g. `v1.0`. The version **does not** depend on the tag, it is taken from the `package_name.__version__` variable.
+ pytest
+ source folder is at the root of the project, and **not** under `src` !
+ `pyproject.toml` used for **everything**

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
