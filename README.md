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

## Building the target package

The template provides enough information to build a `PyPI` and `conda` package, under the `pyproject.toml` and `conda.recipe/meta.yaml` files.

### PyPI

Make sure you have "build" installed, and then you can build the package with:

```
python -m build --outdir dist/ .
```

### Conda

Make sure you have `conda-build` installed, and then you can build the package with:

```
conda config --set anaconda_upload no
conda build -c conda-forge conda.recipe .
```

The previous snippet disables automatic uploading to anaconda. You can see the publishing/uploading part below.

## Publising/Uploading your package

The template includes github actions to automatically publish/upload the packages to `PyPI` and `anaconda.org`, but you can find below the instructions to do it manually as well.

### PyPI
#### PyPI - through github actions

The repository is configured to do the publishing/uploading automatically on `develop` and `main` branches.
You have to enable [trusted publishing](https://docs.pypi.org/trusted-publishers/) from your PyPI account for this to work.
**Hint**: the publisher is the `python-package-deploy.yml`.

#### PyPI - manually

If you prefer to deactivate the automatic github actions, here is how to publish/upload.

1. Install `build` and `twine` in your current or a new environment
2. Configure `twine` with you [pypi username and password](https://twine.readthedocs.io/en/stable/#configuration) and with your [pypi API token](https://pypi.org/help/#apitoken).
3. Run `python -m build` 
4. Run `twine upload dist/*`

You can also consider [uploading to testpypi](https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives) first to test that the process works fine.


### Conda
#### Conda - through github actions

The repository is configured to do the publishing/uploading automatically on `develop` and `main` branches.
You must add 2 secrets to your repository: 

+ `ANACONDA_USER`
+ `ANACONDA_PASSWORD`

#### Conda - manually

1. Install `conda-build` and `anaconda-client` in your current or a new environment
2. Use `anaconda` to login to anaconda.org (see [anaconda documentation](https://docs.anaconda.com/anacondaorg/user-guide/getting-started-with-anaconda-client/) 
3. `conda config --set anaconda_upload yes`
4. Build and upload the package with: `conda build -c conda-forge conda.recipe .`


# Features

+ github actions:
    + test `main` and `develop` on push and on pull requests to this branches on the following:
        + os: [ubuntu-latest, windows-latest, macos-latest] and one version before.
        + py-version: ["3.9", "3.10", "3.11", "3.12"]
    + build source and wheel distribution packages using [build as backend](https://packaging.python.org/en/latest/key_projects/#build)
    + upload to `test.pypi.org` on push events to the `develop` and `main` branches.
    + upload to `pypi.org` on tagged push events to the `develop` and `main` branch with tags.
+ pytest
+ source folder is at the root of the project, and **not** under `src` !
+ `pyproject.toml` used for **everything**

# Requirements

## pre-commit

Follow the instructions at the [pre-commit website](https://pre-commit.com/).

### Install pylint locally

In our pre-commit configuration, we run pylint, and this needs to be installed locally as its Github repo doesn't play nicely with pre-commit.
Follow the instructions at the [pylint website](https://pylint.readthedocs.io/en/latest/user_guide/installation/index.html)
