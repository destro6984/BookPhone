from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView, CreateView
from PhoneBookAdress.forms import AddEmailForm, AddPhoneForm
from PhoneBookAdress.models import Person


class AdressBook(View):
    def get(self, request):
        query = request.GET.get('q')
        if query:
            your_contacts = Person.objects.filter(Q(first_name__lower__contains=query) |
                                                  Q(last_name__lower__contains=query) |
                                                  Q(email__email__contains=query) |
                                                  Q(phone__phone__contains=query)).distinct().order_by("first_name")
        else:
            your_contacts = Person.objects.all().order_by("first_name")
        paginator = Paginator(your_contacts, 7)
        page = request.GET.get('page')
        your_contacts = paginator.get_page(page)
        return render(request, "PhoneBookAdress/Homepage.html", context={"your_contacts": your_contacts})


class PersonCreate(CreateView):
    model = Person
    fields = "__all__"
    success_url = reverse_lazy("homepage")


class PersonUpdate(UpdateView):
    model = Person
    fields = "__all__"
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('homepage')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(request, message="Dane Poprawione")
        return super().post(request, *args, **kwargs)


class DeletePerson(DeleteView):
    model = Person
    success_url = reverse_lazy('homepage')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(request, "Usunięty")
            return redirect("homepage")
        except:
            messages.warning(request, "Brak Dostępu")
            return redirect("homepage")


class AddEmail(View):
    def get(self, request, pk):
        form = AddEmailForm()
        return render(request, "PhoneBookAdress/form.html", context={"form": form})

    def post(self, request, pk):
        form = AddEmailForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.person_id = pk
            email.save()
            messages.success(request, message="Email Dodany")
            return redirect('homepage')


class AddPhone(View):
    def get(self, request, pk):
        form = AddPhoneForm()
        return render(request, "PhoneBookAdress/form.html", context={"form": form})

    def post(self, request, pk):
        form = AddPhoneForm(request.POST)
        if form.is_valid():
            phone = form.save(commit=False)
            phone.person_id = pk
            phone.save()
            messages.success(request, message="Telefon Dodany")
            return redirect('homepage')
        else:
            messages.warning(request, message="Błędny numer Telefonu")
            return redirect('addphone', pk=pk)

