from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Define a root API endpoint
@api_view(['GET'])
def api_root(request):
    return Response({
        "movies": "/api/movies/",
        "tvshows": "/api/tvshows/",
        "watchlist": "/api/watchlist/",
        "search": "/api/search/",
        "users": "/api/users/",
        "token": "/api/token/",
        "token_refresh": "/api/token/refresh/",
    })

urlpatterns = [
    path('', api_root, name='api-root'),  # Root API page
    path('admin/', admin.site.urls),
    path('api/', include('apps.movies.urls')),
    path('api/', include('apps.users.urls')),

    # JWT Authentication Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]