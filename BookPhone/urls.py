"""PhoneBookAdress URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from PhoneBookAdress.views import AdressBook, PersonUpdate, DeletePerson, AddEmail, AddPhone, PersonCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AdressBook.as_view(), name='homepage'),
    path('update/<pk>', PersonUpdate.as_view(), name='update'),
    path('delete/<pk>', DeletePerson.as_view(), name='delete'),
    path('addemail/<pk>', AddEmail.as_view(), name='addemail'),
    path('addphone/<pk>', AddPhone.as_view(), name='addphone'),
    path('create/', PersonCreate.as_view(), name='create'),
]
