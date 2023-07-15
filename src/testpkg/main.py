"""
main.py
"""
from dataclasses import dataclass
from importlib.metadata import PackageNotFoundError, version

import numpy as np

PACKAGE_NAME = "testpkg"

INF = np.Inf


def square(number: float) -> float:
    """Square a number."""
    return number * number


@dataclass
class MyClass:
    """My Class."""

    name: str
    number: float

    @property
    def square(self) -> float:
        """Square my number."""
        return square(self.number)


def hello() -> int:
    """Show version and say hello."""
    try:
        version_ = version(PACKAGE_NAME)
        print(f"{PACKAGE_NAME} version {version_}")
    except PackageNotFoundError:
        print(f"Package {PACKAGE_NAME} not installed.")
    print("Hello, world!")
    return 0


if __name__ == "__main__":
    raise SystemExit(hello())
