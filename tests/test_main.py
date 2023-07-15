"""
test_main.py
"""

from testpkg import main


def test_square() -> None:
    """Test main.square."""
    assert main.square(2) == 4
