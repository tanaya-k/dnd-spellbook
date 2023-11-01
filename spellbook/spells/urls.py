from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("<int:spell_id>/", views.description, name="description"),
]