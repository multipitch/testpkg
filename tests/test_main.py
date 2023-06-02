"""
test_main.py
"""

from testpkg import main


def test_square():
    """Test main.square."""
    assert main.square(2) == 4
