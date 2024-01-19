from django import forms
from .models import Category, User, News


class CategoriesForm(forms.Form):
    name = forms.CharField(
        label='Nome',
        max_length=200,
        required=True,
    )


class CreateNewsModelForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"

        labels = {
            "title": "Título",
            "content": "Conteúdo",
            "author": "Autoria",
            "created_at": "Criado em",
            "image": "URL da Imagem",
            "categories": "Categorias"
        }

        widgets = {
            "content": forms.Textarea(attrs={'rows': 5}),
            "created_at": forms.DateInput(attrs={'type': 'date'}),
            "image": forms.FileInput,
        }

    def __init__(self, *args, **kwargs):
        super(CreateNewsModelForm, self).__init__(*args, **kwargs)

        self.fields['author'].widget = forms.Select()
        self.fields['categories'].widget = forms.CheckboxSelectMultiple()
        self.fields['author'].queryset = User.objects.all()
        self.fields['categories'].queryset = Category.objects.all()
        self.fields['author'].required = True
        self.fields['categories'].required = True
