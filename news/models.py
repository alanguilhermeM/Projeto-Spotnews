from django.db import models
from django.core.exceptions import ValidationError


def validate_min_words(value):
    words = value.split()
    if len(words) < 2:
        raise ValidationError(
            _('O título deve ter mais de uma palavra.'),
            code='invalid_title',
        )


class Category(models.Model):
    name = models.CharField(max_length=200, blank=False)

    def __str__(self) -> str:
        return f'{self.name}'


class User(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    password = models.CharField(max_length=200, blank=False)
    role = models.CharField(max_length=200, blank=False)

    def __str__(self) -> str:
        return f'{self.name}'


class News(models.Model):
    title = models.CharField(
        max_length=200,
        blank=False,
        validators=[validate_min_words]
    )
    content = models.TextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, blank=False)
    image = models.ImageField(upload_to='images/', blank=True)
    categories = models.ManyToManyField(Category, blank=False)

    def __str__(self) -> str:
        return self.title
