
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from InternApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('add_pizza/',views.add_pizza),
    url('show_pizza/',views.show_pizza),
    url('update_pizza/',views.update_pizza),
    url('delete_pizza/',views.delete_pizza),
    url('filter_pizzas/',views.filter_pizzas),
]
