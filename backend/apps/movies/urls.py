from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'watchlist', views.WatchListViewSet, basename='watchlist')
router.register(r'movies', views.MovieViewSet)
router.register(r'tv-shows', views.TVShowViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Fetch media related to movies
    path('movies/popular/', views.fetch_movies, {'selection': 'popular'}, name='fetch_movies_popular'),
    path('movies/now-playing/', views.fetch_movies, {'selection': 'now_playing'}, name='fetch_movies_now_playing'),
    path('movies/upcoming/', views.fetch_movies, {'selection': 'upcoming'}, name='fetch_movies_upcoming'),
    path('movies/top-rated/', views.fetch_movies, {'selection': 'top_rated'}, name='fetch_movies_top_rated'),

    # Fetch media related to TV shows
    path('tv-shows/popular/', views.fetch_tvshows, {'selection': 'popular'}, name='fetch_tvshows_popular'),
    path('tv-shows/airing-today/', views.fetch_tvshows, {'selection': 'airing_today'}, name='fetch_tvshows_airing_today'),
    path('tv-shows/on-tv/', views.fetch_tvshows, {'selection': 'on_tv'}, name='fetch_tvshows_on_tv'),
    path('tv-shows/top-rated/', views.fetch_tvshows, {'selection': 'top_rated'}, name='fetch_tvshows_top_rated'),

    # Search media (movies or TV shows)
    path('search/', views.search_media, name='search_media'),
]