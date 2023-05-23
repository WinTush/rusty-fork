# rustyfork

[![fuzzy-couscous](https://img.shields.io/badge/built%20with-fuzzy--couscous-success)](https://github.com/Tobi-De/fuzzy-couscous)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code style: djlint](https://img.shields.io/badge/html%20style-djlint-blue.svg)](https://www.djlint.com)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)

Website for the Rusty Fork, a local neighbourhood distro.

## Prerequisites

- `Python 3.10+`
- `Postgresql 10+`

## Development

### Create and activate a new virtual environment

```shell
python3 -m venv --prompt . venv
source venv/bin/activate
```

### Install dependencies

```shell
python3 -m pip install -r dev-requirements.txt
```

### Install pre-commit

```shell
pre-commit install
```

### Populate environment variables

```shell
cp .env.template .env
```

### Run the django development server

```
poe r
```

[poethepoet](https://github.com/nat-n/poethepoet) is the task runner used here. To see all available commands read
the `[tool.poe.tasks]`section of the `pyproject.toml` file or run `poe -h` to see the help page.

> **Note**: SITE_ID
>
> You may get an error when trying to login or signup, this is due to django-allauth, you need to create a new _site_ in django
> admin and use its _ID_ as the value of `SITE_ID` in the `settings.py`file.
> Create a new superuser with the `python manage.py createsuperuser` command, login to django admin then look for the `sites`
> section in the left navigation bar and create a new _site_.
