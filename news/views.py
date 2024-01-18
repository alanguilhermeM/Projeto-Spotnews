from django.shortcuts import render, redirect
from .models import News, Category
from django.shortcuts import get_object_or_404
from django.http import Http404
from .forms import CategoriesForm, NewsForm


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


def news_form(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)

        if form.is_valid():
            new_instance = News(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                author=form.cleaned_data['author'],
                created_at=form.cleaned_data['created_at'],
                image=request.FILES.get('image'),
            )
            new_instance.save()
            new_instance.categories.set(form.cleaned_data['categories'])
            return redirect('home-page')
    else:
        form = NewsForm()
    context = {'forms': form}
    return render(request, 'news_form.html', context)
