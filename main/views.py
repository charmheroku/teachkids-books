from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.flatpages.models import FlatPage

from main.forms import ApplicationForm

from .models import Category


def main_page(request):
    """Отображение главной страницы сайта"""

    return render(request, "main/index.html")


def category_page(request, slug):
    """Отображение страницы категорий"""
    try:
        books_category = Category.objects.get(slug=slug)

    except Category.DoesNotExist:
        return redirect(reverse("main_page"))
    return render(request, "main/category.html", {"books_category": books_category})


def contact(request):
    contact_flatpage = get_object_or_404(FlatPage, url="/contact/")

    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you for your request! We will contact you as soon as possible",
            )
            return redirect(reverse("main:contact_page"))
    else:
        form = ApplicationForm()

    return render(
        request,
        "flatpages/contacts.html",
        {
            "form": form,
            "flatepage": contact_flatpage,
        },
    )
