# testpkg
A basic project layout.

## Developing
```
$ git clone https://github.com/multipitch/testpkg.git
$ cd testpkg
$ pyenv local 3.11 3.8 3.9 3.10
$ python -m venv .venv
$ . .venv/bin/activate
$ pip install --upgrade pip setuptools
$ pip install -r requirements-dev.txt
```
Note: list primary python version first in above `pyenv` command.
The other versions are required for nox.

## Linting and Formatting
- If using VSCode, the included config should automatically lint & format on save.
- Pre-commit will run a suite of linters & formatters on commits.

## Testing
- Run `nox` to test package.

## Notes
- VSCode configuration files should generally not be commited in real projects.
  The file has been incldued here to show some recommended settings.

## TODO
- Building/publishing with pipelines
- Dev vs Main branches - automatic building and tagging on merge with main?
- Documentation
- Documentation hosting
- Guide for how to edit, test, commit, merge, tag, publish, etc.
