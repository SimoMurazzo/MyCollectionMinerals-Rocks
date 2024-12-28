# MyMineralCollection
Web app Django-based to store, manage and show your mineral collection

Copyright (C) 2024  Simone Murazzo

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

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
