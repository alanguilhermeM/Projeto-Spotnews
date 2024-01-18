from django.shortcuts import render, redirect
from .models import News, Category
from django.shortcuts import get_object_or_404
from django.http import Http404
from .forms import CategoriesForm


# Create your views here.
def index(request):
    context = {"news": News.objects.all()}
    return render(request, 'home.html', context)


def news_details(request, id):
    try:
        new = get_object_or_404(News, id=id)
        return render(request, 'news_details.html', {'new': new})
    except Http404:
        return render(request, '404.html')


def categories_form(request):
    if request.method == 'POST':
        form = CategoriesForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            category = Category(name=name)
            category.save()
            return redirect('home-page')
    else:
        form = CategoriesForm()
    context = {'forms': form}
    return render(request, 'categories_form.html', context)
