from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'watchlist', views.WatchListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('movies/<str:category>/', views.fetch_movies),
    path('search/', views.search_media),
]
