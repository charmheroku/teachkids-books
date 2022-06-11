from django.urls import path

from main import views

app_name = "main"

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("category/<slug:slug>/", views.category_page, name="category_page"),
    path("contact/", views.contact, name="contact_page"),
]
