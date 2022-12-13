# cookiecutter-brightwaylib

A cookiecutter based project template for Brightway ecosystem packages.

# Usage

This is a cookiecutter based template to create Brightway ecosystem packages.
The regular usage instructions from cookiecutter apply:

1. Install cookiecutter
2. Invoke cookiecutter passing either this repository as URL or a cloned local directory.

```
cookiecutter cookiecutter-brightwaylib/
```

# Features

+ github actions to upload pypi package
+ pytest
+ source folder is at the root of the project, and **not** under `src` !
+ `pyproject.toml` used for **configuring the build system only**
+ `setup.cfg` contains the configuration of the package (name, install_requires, metadata)


# Information you need before using the cookie cutter

You will need to answer questions regarding:

+ You (full name, email, github_username)
+ the project name (brightway2-data for example)
+ the package name (bw2data for example)
+ A project description
+ A pypi user name
+ starting project version (by default 0.1.0)
+ Using "click" as CLI library
+ Which open source library to use. If you don't select MIT, you need to supply the contents and file (LICENSE) for the other options.

