from django.db import models


class Anime(models.Model):
    name = models.CharField(max_length=50)