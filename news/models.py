from django.db import models
from django.core.exceptions import ValidationError


def validate_min_words(value):
    words = value.split()
    if len(words) < 2:
        raise ValidationError(
            ('O título deve conter pelo menos 2 palavras.'),
            code='invalid_title',
        )
    if not value:
        raise ValidationError(
            {"title": ["Este campo não pode estar vazio."]}
        )


def valid_content(value):
    if not value:
        raise ValidationError(
            {"content": ["Este campo não pode estar vazio."]}
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
    content = models.TextField(blank=False, validators=[valid_content])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=False)
    image = models.ImageField(upload_to='images/', blank=True)
    categories = models.ManyToManyField(Category, blank=False)

    def __str__(self) -> str:
        return self.title
