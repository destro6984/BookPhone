from django.forms import ModelForm

from PhoneBookAdress.models import Person


class AddPerson(ModelForm):
    class Meta:
        model=Person
        fields = "__all__"


