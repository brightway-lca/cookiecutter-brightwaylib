"""{{cookiecutter.package_name}}."""
from {{ cookiecutter.package_name }}.utils import get_version_tuple

__all__ = (
    "__version__",
    # Add functions and variables you want exposed in `{{cookiecutter.package_name}}.` namespace here
)

__version__ = get_version_tuple()
