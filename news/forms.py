from django import forms
from .models import Category, User


class CategoriesForm(forms.Form):
    name = forms.CharField(
        label='Nome',
        max_length=200,
        required=True,
        # widget=forms.TextInput(attrs={'type': 'text', 'name': 'name'})
    )


class NewsForm(forms.Form):
    title = forms.CharField(label='Título')

    content = forms.CharField(
        label='Conteúdo',
        widget=forms.Textarea(attrs={'rows': 5})
    )

    author = forms.ModelChoiceField(
        label='Autoria',
        queryset=User.objects.all()
    )

    created_at = forms.DateField(
        label='Criado em',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    image = forms.ImageField(
        label='URL da Imagem',
        required=False,
        widget=forms.FileInput
    )

    categories = forms.ModelMultipleChoiceField(
        label='Categorias',
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
