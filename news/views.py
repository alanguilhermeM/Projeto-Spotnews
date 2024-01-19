from django.shortcuts import render, redirect
from .models import News, Category, User
from django.shortcuts import get_object_or_404
from django.http import Http404
from .forms import CategoriesForm, CreateNewsModelForm
from rest_framework import viewsets
from .serializers import CategorySerializer, UserSerializer, NewsSerializer


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
        form = CreateNewsModelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = CreateNewsModelForm()
    context = {'forms': form}
    return render(request, 'news_form.html', context)


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
