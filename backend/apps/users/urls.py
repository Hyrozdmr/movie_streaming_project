from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, WatchlistViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'watchlist', WatchlistViewSet, basename='watchlist')

urlpatterns = [
    path('', include(router.urls)),
]