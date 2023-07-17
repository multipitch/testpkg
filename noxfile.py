"""
noxfile.py
"""

import nox

SUPPORTED_VERSIONS = ["3.9", "3.10", "3.11"]
MAIN_VERSION = "3.11"


@nox.session(python=MAIN_VERSION)
def lint(session: nox.Session) -> None:
    """Run pre-commit."""
    session.install("-r", "requirements-dev.txt")
    session.run("pre-commit", "run", "--all-files")


@nox.session(python=SUPPORTED_VERSIONS)
def test(session: nox.Session) -> None:
    """Run tests."""
    session.install(".")
    session.install("pytest-cov")
    session.run("pytest", "--cov")


@nox.session(python=MAIN_VERSION)
def build(session: nox.Session) -> None:
    """Run build."""
    session.install("build")
    session.run("python", "-m", "build", "--wheel")


@nox.session(python=MAIN_VERSION)
def publish(session: nox.Session) -> None:
    """Run twine."""
    session.install("twine")
    session.run(
        "twine", "upload", "--repository", "testpypi", "--skip-existing", "dist/*"
    )
