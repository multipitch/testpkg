"""
init.py
"""
from importlib.metadata import PackageNotFoundError, version

from .main import MyClass, hello, square

__all__ = ["MyClass", "hello", "square"]

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    pass
