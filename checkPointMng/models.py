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
