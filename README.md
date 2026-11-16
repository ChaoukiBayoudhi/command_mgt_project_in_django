# Command management project in Django

A Django project with 3 models.

## Tech stack

- Python 3
- Django
- Database: SQLite

## Project structure

- `command_mgt_project/`: project settings and root URLs
- `command_app/`: Django app
- Tests: `command_app/tests.py`

## Data model

| Model | App | Fields |
|---|---|---|
| `Product` | `command_app` | label, price, stock |
| `Client` | `command_app` | name, birthDate, client_products |
| `Command` | `command_app` | prod, clt, date, quantity |

## URL routes

Declared in `urls.py`:

- `/blog/`

## How to run

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py runserver
```

There is no `requirements.txt`; the packages above are the ones the settings and imports refer to.

Then open `http://127.0.0.1:8000/`.

---

Author: [Chaouki Bayoudhi](https://github.com/ChaoukiBayoudhi)
