from django.db import models


class Sheet(models.Model):
    num = models.IntegerField()
    order = models.IntegerField()
    price = models.IntegerField()
    date = models.TextField()

    class Meta:
        ordering = ['id']






