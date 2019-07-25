import random, django, os

from django.db import IntegrityError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BookPhone.settings")
django.setup()
from PhoneBookAdress.models import Person, Email, Phone
from faker import Faker


def create_persons(n):
    fake = Faker()
    for _ in range(25):
        id = random.randint(1, 50)
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone = fake.numerify('###-###-###')
        try:
            Person.objects.create(id=id, first_name=first_name, last_name=last_name)
        except IntegrityError:
            continue
        Email.objects.create(email=email, person_id=id)
        Phone.objects.create(phone=phone, person_id=id)
    return "Added"
