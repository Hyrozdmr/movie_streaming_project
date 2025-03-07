from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'movies', views.FetchMoviesViewSet, basename='movie')
router.register(r'tvshows', views.FetchTVShowsViewSet, basename='tvshow')
router.register(r'watchlist', views.WatchListViewSet, basename='watchlist')
router.register(r'search', views.SearchMediaViewSet, basename='search')  # New search ViewSet

urlpatterns = [
    path('', include(router.urls)),  # Registers all ViewSet routes
]