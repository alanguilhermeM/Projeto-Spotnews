from django import forms


class CategoriesForm(forms.Form):
    name = forms.CharField(
        label='Nome',
        max_length=200,
        required=True,
        # widget=forms.TextInput(attrs={'type': 'text', 'name': 'name'})
    )
