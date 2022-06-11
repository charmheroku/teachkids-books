from django import template

register = template.Library()


@register.filter
def filter_books(category):
    """Тэг фильтрации книг в категории"""
    filtered_books = category.books.filter(is_published=True)
    return filtered_books


