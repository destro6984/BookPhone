from django.db import models


# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"first_name: {self.first_name}, last_name: {self.last_name}"


class PersonInfo(models.Model):
    person = models.ForeignKey(Person, editable=False,on_delete=models.PROTECT)
    phone = models.CharField(max_length=50)
    email = models.EmailField()


# class Email(models.Model):
#     person = models.ForeignKey(Person, editable=False)
#     email = models.EmailField()
