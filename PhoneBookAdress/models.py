from django.db import models


# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"first_name: {self.first_name}, last_name: {self.last_name} phone: {self.phone_set.all()}, email: {self.email_set.all()}"


class Phone(models.Model):
    person = models.ForeignKey(Person, editable=False,on_delete=models.PROTECT)
    phone = models.CharField(max_length=50)


    def __str__(self):
        return f"phone: {self.phone}"

class Email(models.Model):
    person = models.ForeignKey(Person, editable=False,on_delete=models.PROTECT)
    email = models.EmailField()
    def __str__(self):
        return f"email: {self.email}"
