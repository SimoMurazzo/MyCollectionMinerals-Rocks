# MyCollectionMinerals-Rocks
Web app Django-based to store, manage and show your collection of minerals / rocks

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

Install Git and [uv](https://docs.astral.sh/uv/).

```
$ git clone https://github.com/SimoMurazzo/MyCollectionMinerals-Rocks.git
$ cd MyCollectionMinerals-Rocks
$ uv sync --locked
$ uv run manage.py migrate
$ export DJANGO_SUPERUSER_PASSWORD=password
$ uv run manage.py createsuperuser --no-input --username admin
$ uv run manage.py runserver
```
