from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'tv-shows', views.TVShowViewSet)
router.register(r'watchlist', views.WatchListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('popular/', views.fetch_popular_media),
    path('now-playing/', views.fetch_now_playing_media),
    path('upcoming/', views.fetch_upcoming_media),
    path('search/', views.search_media),
]