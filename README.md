![example event parameter](https://github.com/profusionuk/python-best-practice/actions/workflows/main.yml/badge.svg)
[![Python Version](https://img.shields.io/badge/python-3.9-brightgreen.svg)](https://python.org)

# Project instructions

## Create a README.md file
Place the file in the root directory.

### Markdown Cheat Sheet
[https://www.markdownguide.org/cheat-sheet/](https://www.markdownguide.org/cheat-sheet/)

### Always add a .gitignore file
This is the default used in Python.
[https://github.com/github/gitignore/blob/master/Python.gitignore](https://github.com/github/gitignore/blob/master/Python.gitignore)

### While the above .gitignore has .env by default, it is of importance to add "env.ini" to this file to avoid adding sensitive details to the repo.

### Always add a .env file
This file holds secure information that should never go into the source code repository.

Run your app in a Virtual Environment: [http://python-guide-ru.readthedocs.io/en/latest/dev/virtualenvs.html](http://python-guide-ru.readthedocs.io/en/latest/dev/virtualenvs.html)

### For best practice install python-decouple, black and isort

The package python-decouple handles the .env / .ini files, and black is a code formatting tool, 
isort is a utility to sort imports alphabetically, and automatically separated into sections and by type.
```shell
pip install python-decouple black isort
```

[https://pypi.org/project/python-decouple/](https://pypi.org/project/python-decouple/)

[https://black.readthedocs.io/en/stable/index.html](https://black.readthedocs.io/en/stable/index.html)

[https://pycqa.github.io/isort/](https://pycqa.github.io/isort/)

IDE set up guide for Black Python code formatting.
[https://black.readthedocs.io/en/stable/integrations/editors.html](https://black.readthedocs.io/en/stable/integrations/editors.html)

### All Python projects should contain a requirements.txt file

### Each directory containing .py files should also have as below, this makes the directory a Python package 
```shell
__init__.py
``` 

### Run main app module
```shell
python -m main
```

### Unit / Functional tests

Use Pytest: 
[https://docs.pytest.org/en/latest/](https://docs.pytest.org/en/latest/)

Add pytest and coverage:
```shell
pip install pytest pytest-cov
```

[https://pypi.org/project/pytest-cov/](https://pypi.org/project/pytest-cov/)

Run pytest with verbose flag:
```shell
pytest -v
```

Run with coverage from root directory:
```shell
coverage report -m
```

Run pytest-cov on chosen directories:
```shell
pytest --cov=db --cov=bucket --cov=api --cov-report html
```

### Moto serverless mock testing framework
[http://docs.getmoto.org/en/latest/docs/getting_started.html](http://docs.getmoto.org/en/latest/docs/getting_started.html)

```shell
pip install moto
```

### Type hints in Python
[https://docs.python.org/3/library/typing.html](https://docs.python.org/3/library/typing.html)

In Python 3.5 type hints were added example usage below:
```shell
def greeting(name: str) -> str:
    return f"Hello {name}" 
```

### Added GitHub Actions for the CI (Continuous Integration) Process
In the root directory we have .github/worklfows/ directories
with a main.yml file that will run on each commit, via the repo, click on the Actions tab to see all builds.