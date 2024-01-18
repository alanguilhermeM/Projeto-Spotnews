from django.urls import path
from news.views import index, news_details, categories_form, news_form


urlpatterns = [
    path("", index, name="home-page"),
    path("news/<int:id>", news_details, name="news-details-page"),
    path("categories/", categories_form, name="categories-form"),
    path("news/", news_form, name="news-form")
]
