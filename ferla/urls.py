from django.urls import path

from ferla.views import mestre_ferla




urlpatterns = [
    path("ferla/", mestre_ferla, name="ferla")
]
