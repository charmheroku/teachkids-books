from django.db import models
from django.core.validators import FileExtensionValidator

from ckeditor.fields import RichTextField

from django.contrib.flatpages.models import FlatPage


class CustomFlatePage(FlatPage):
    cover = models.ImageField(
        verbose_name="Image for page", upload_to="flatpages", default="", blank=True
    )


class Category(models.Model):
    """Модель категорий"""

    name = models.CharField(max_length=100, verbose_name="Name")
    text = RichTextField(verbose_name="Text", default="")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Slug")
    cover = models.ImageField(
        verbose_name="Image for category", upload_to="categories", default=""
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Book(models.Model):
    """Модель Books"""

    title = models.CharField(max_length=255)
    text = RichTextField(verbose_name="Text", default="")

    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name="Slug",
        help_text="This field autofill",
    )

    cover = models.ImageField(
        verbose_name="Image for book", upload_to="books", default=""
    )

    category = models.ForeignKey(
        "Category",
        verbose_name="Category",
        related_name="books",
        on_delete=models.PROTECT,
    )
    is_published = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return str(self.title)


class BookFile(models.Model):

    LESSON_FORMAT = "1"
    VISUALS_FORMAT = "2"
    RESOURCE_PACK_FORMAT = "3"
    FORMAT_CHOICES = (
        (LESSON_FORMAT, "Lesson Text"),
        (VISUALS_FORMAT, "Visuals"),
        (RESOURCE_PACK_FORMAT, "Resource pack"),
    )

    file = models.FileField(
        verbose_name="Book file",
        upload_to="books_files",
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
    )
    format_book = models.CharField(
        choices=FORMAT_CHOICES,
        max_length=20,
        default=LESSON_FORMAT,
    )
    book = models.ForeignKey(
        "Book", on_delete=models.CASCADE, related_name="book_files"
    )

    def __str__(self):
        return self.book.title

    class Meta:
        verbose_name = "Book File"
        verbose_name_plural = "Book Files"


class Application(models.Model):
    """Модель сбора заявок с сайта"""

    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    agreement = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Сбор заявок с сайта"
        verbose_name_plural = "Сбор заявок с сайта"

    def __str__(self):
        return str(self.name)
