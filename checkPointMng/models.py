from django import forms
from django.db import models

# following commands after making any changes:
#   cd bookEx (\, PythonSpace, checkPoint)
#   python manage.py makemigrations
#   python manage.py migrate


class MainMenu(models.Model):
    item = models.CharField(max_length=200, unique=True)
    link = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.item


LAX_TERMINALS = (
    ("Suites", "Suites"),
    ("TBIT Main Checkpoint", "TBIT Main Checkpoint"),
    ("Terminal 1 - Passenger", "Terminal 1 - Passenger"),
    ("Terminal 2 - Passenger", "Terminal 2 - Passenger"),
    ("Terminal 3 - Passenger", "Terminal 3 - Passenger"),
    ("Terminal 4 - FIS", "Terminal 4 - FIS"),
    ("Terminal 4 - Passenger", "Terminal 4 - Passenger"),
    ("Terminal 4a - Passenger", "Terminal 4a - Passenger"),
    ("Terminal 5 - Passenger", "Terminal 5 - Passenger"),
    ("Terminal 5a - Passenger", "Terminal 5a - Passenger"),
    ("Terminal 6 - Passenger", "Terminal 6 - Passenger"),
    ("Terminal 7 - Passenger", "Terminal 7 - Passenger"),
)


class DateInput(forms.DateInput):
    input_type = 'date'


class Search(models.Model):
    terminal = models.CharField(max_length=23, choices=LAX_TERMINALS)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return str(self.id)