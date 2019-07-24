from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import UpdateView
from django.views.generic.base import View

from PhoneBookAdress.forms import AddPerson
from PhoneBookAdress.models import Person


class AdressBook(View):
    def get(self,request):
        your_contacts= Person.objects.all()
        form_add_person=AddPerson()
        return render(request, "PhoneBookAdress/Homepage.html", context={"form_add_person":form_add_person,
                                                                   "your_contacts":your_contacts})

    def post(self, request):
        form_add_person = AddPerson(request.POST)
        if form_add_person.is_valid():
            form_add_person.save()
            messages.success(request, message="Osoba Dodana")
            return redirect('homepage')


class PersonUpdate(UpdateView):
    model = Person
    fields = "__all__"
    template_name_suffix = '_update_form'