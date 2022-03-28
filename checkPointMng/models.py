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
    ("Terminal 4A - Passenger", "Terminal 4A - Passenger"),
    ("Terminal 5 - Passenger", "Terminal 5 - Passenger"),
    ("Terminal 5A - Passenger", "Terminal 5A - Passenger"),
    ("Terminal 6 - Passenger", "Terminal 6 - Passenger"),
    ("Terminal 7 - Passenger", "Terminal 7 - Passenger"),
)


class Airport(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=3, unique=True)


class Terminal(models.Model):
    name = models.CharField(max_length=200, unique=True)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)


class Throughput(models.Model):

    date = models.DateTimeField()
    throughput = models.IntegerField()

    @property
    def logs(self):
        return self.date, self.throughput


class AirportThroughput(models.Model):
    date = models.DateTimeField()
    throughput = models.IntegerField()
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)


class TerminalThroughput(models.Model):
    date = models.DateTimeField()
    throughput = models.IntegerField()
    terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)


class DateInput(forms.DateInput):
    input_type = 'date'


class Search(models.Model):
    terminal = models.CharField(max_length=23, choices=LAX_TERMINALS)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return str(self.id)