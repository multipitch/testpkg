# testpkg
A basic project layout.

## Developing
Assumes we are working on linux.
Assumes [pyenv](https://github.com/pyenv/pyenv) is available and relevant python versions are installed.
```
$ git clone https://github.com/multipitch/testpkg.git
$ cd testpkg
$ pyenv local 3.11 3.8 3.9 3.10
$ python -m venv .venv
$ . .venv/bin/activate
$ python -m pip install --upgrade pip setuptools
$ python -m pip install -r requirements-dev.txt
$ python -m pip install -e .
```
Note: list the primary python version first in above `pyenv` command.
The other versions are just used fortesting purposes.

## Formatting and Linting
- If using VSCode, the included config should automatically lint & format on save.
  - Note that the VSCode config file is usually not commited, but is inculded here for info.
- Run `nox -s lint` to format and lint all code (this will run automatically on commits also).

## Testing
- Run `nox -s test` to test package.

## Versioning
- Versions are derived from git tags
- Before building a new release, generate a tag (e.g. for version 1.2.3)
  ```
  $ git tag -a v1.2.3 -m "version 1.2.3"
  $ git push origin v1.2.3
  ```
## Building
- Run `nox -s build` to build the package.

## Publishing
- Run `nox -s publish` to publish the package to the pypi testing repo.
- You can create a .pypirc file in ~ to store login credentials.
- Do not store credentials in this repo.


## TODO
- Building/publishing with pipelines/actions
- Rename so can upload to pypi testing
- Build version relies on tag
- Best practise for branches? Use a dev branch?
- Documentation
- Documentation hosting
- Guide for how to edit, test, commit, merge, tag, publish, etc.
