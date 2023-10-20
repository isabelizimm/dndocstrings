# Set version ----
from importlib_metadata import version as _v

__version__ = _v("dndocstrings")

del _v

from .classes import TestClass
from .docstrings import (
    rest,
    epytext,
    google,
    numpy_scipy
)
