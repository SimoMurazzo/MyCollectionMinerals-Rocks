# MyMineralCollection
Web app Django-based to store, manage and show your mineral collection

## First run (only in development mode)

Install Git, Python and pip.

```
$ git clone https://github.com/SimoMurazzo/MyMineralCollection.git
$ cd MyMineralCollection
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install wheel
$ pip install --no-deps --require-hashes -r requirements.txt
$ python manage.py migrate
$ export DJANGO_SUPERUSER_PASSWORD=password
$ python manage.py createsuperuser --no-input --username admin
$ python manage.py runserver
```
