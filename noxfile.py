"""
noxfile.py
"""

import nox


@nox.session(python=["3.8", "3.9", "3.10", "3.11"])
def test(session: nox.Session) -> None:
    """Run tests."""
    session.install(".")
    session.install("pytest-cov")
    session.run("pytest", "--cov")
