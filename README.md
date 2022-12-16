# cookiecutter-brightwaylib

A [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/index.html) based project template for Brightway ecosystem packages.

# [Usage](https://cookiecutter.readthedocs.io/en/stable/usage.html)

1. Create a new environment (pip or conda), activate it, and install `cookiecutter`
2. Download (i.e. don't install via pip or conda) this repository, either directly or via git
3. Edit the `cookiecutter.json` file to give your personal info. You should update at least:

* "full_name"
* "email"
* "github_username"

4. Invoke cookiecutter *in the parent directory of `cookiecutter-brightwaylib`*

```
cookiecutter cookiecutter-brightwaylib/
```

# Features

+ github actions:
    + test `main` and `develop` on push and on pull requests to this branches on the following:
        + os: [ubuntu-latest, windows-latest, macos-latest]
        + py-version: ["3.8", "3.9", "3.10", "3.11"]
    + build source and wheel distribution packages using [build as backend](https://packaging.python.org/en/latest/key_projects/#build)
    + upload to `test.pypi.org` on push events to the `develop` branch
    + upload to `pypi.org` on **tagged** push events to the `main` branch. The version **does not** depend on the tag.
+ pytest
+ source folder is at the root of the project, and **not** under `src` !
+ `pyproject.toml` used for **configuring the build system only**
+ `setup.cfg` contains the configuration of the package (name, install_requires, metadata)


# Requirements

## Secrets for publishing
The github actions to publish to test.pypi.org and pypi.org require the creation of the following 2 secrets:

+ `TEST_PYPI_API_TOKEN`
+ `PYPI_API_TOKEN`

No username is necessary because the github action uses the new `__token__` based approach.
The previous secrets are the tokens generated through the test.pypi.org and pypi.org sites.
See [uploading distribution archives](https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives) for more information.

## Information you need before using the cookie cutter

You will need to answer questions regarding:

+ You (full name, email, github_username)
+ the project name (`brightway2-data` for example). This corresponds to a github repository name. Make sure you don't use spaces.
+ the package name (`bw2data` for example)
+ A project description
+ starting project version (by default 0.1.0)
+ Using "click" as CLI library
+ Which open source license to use.
