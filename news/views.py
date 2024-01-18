from django.shortcuts import render
from .models import News
from django.shortcuts import get_object_or_404
from django.http import Http404


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
