from django.urls import path, include
from news.views import index, news_details, categories_form, news_form
from rest_framework import routers
from .views import CategoriesViewSet, UsersViewSet, NewsViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoriesViewSet)
router.register(r'users', UsersViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = [
    path("", index, name="home-page"),
    path("news/<int:id>", news_details, name="news-details-page"),
    path("categories/", categories_form, name="categories-form"),
    path("news/", news_form, name="news-form"),
    path("api/", include(router.urls))
]
