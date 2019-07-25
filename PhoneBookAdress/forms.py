from django.core.validators import RegexValidator
from django.forms import ModelForm
from django import forms

from PhoneBookAdress.models import Email, Phone


class AddEmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ['email']


class AddPhoneForm(ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ddd-ddd-ddd'}),validators=[RegexValidator("^\d{3}[-]\d{3}[-]\d{3}$")])
    class Meta:
        model = Phone
        fields = ['phone']


