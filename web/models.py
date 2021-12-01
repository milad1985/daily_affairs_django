from django.db import models
from django.contrib.auth.models import AnonymousUser, User


# Create your models here.


class Expense(models.Model):
    name = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} -- {}".format(self.name, self.amount)


class Income(models.Model):
    name = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} -- {}".format(self.name, self.amount)
