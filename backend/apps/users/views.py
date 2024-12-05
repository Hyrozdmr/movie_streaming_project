from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User, WatchList
from apps.movies.models import Movie, TVShow
from .serializers import UserSerializer, WatchlistSerializer
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)


class WatchlistViewSet(viewsets.ModelViewSet):
    serializer_class = WatchlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return the watchlist for the authenticated user
        return WatchList.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Save the watchlist item for the authenticated user
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'], url_path='add-to-watchlist')
    def add_to_watchlist(self, request, pk=None):
        # Handle adding a movie or tv show to the user's watchlist
        media_id = request.data.get('media_id')
        media_type = request.data.get('media_type')  # 'movie' or 'tv'

        if not media_id or not media_type:
            return Response({"error": "Media ID and type are required."}, status=status.HTTP_400_BAD_REQUEST)

        user = self.request.user
        watchlist_item = None

        if media_type == 'movie':
            movie = Movie.objects.filter(tmdb_id=media_id).first()
            if movie:
                watchlist_item, created = WatchList.objects.get_or_create(user=user, movie=movie)
        elif media_type == 'tv':
            tv_show = TVShow.objects.filter(tmdb_id=media_id).first()
            if tv_show:
                watchlist_item, created = WatchList.objects.get_or_create(user=user, tv_show=tv_show)
        
        if watchlist_item:
            if created:
                return Response(WatchlistSerializer(watchlist_item).data, status=status.HTTP_201_CREATED)
            return Response({"message": "Item already in watchlist."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Media not found."}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'], url_path='remove-from-watchlist')
    def remove_from_watchlist(self, request, pk=None):
        # Handle removing a movie or tv show from the user's watchlist
        media_id = request.data.get('media_id')
        media_type = request.data.get('media_type')  # 'movie' or 'tv'

        if not media_id or not media_type:
            return Response({"error": "Media ID and type are required."}, status=status.HTTP_400_BAD_REQUEST)

        user = self.request.user
        if media_type == 'movie':
            movie = Movie.objects.filter(tmdb_id=media_id).first()
            if movie:
                try:
                    watchlist_item = WatchList.objects.get(user=user, movie=movie)
                    watchlist_item.delete()
                    return Response({"message": "Movie removed from watchlist."}, status=status.HTTP_200_OK)
                except WatchList.DoesNotExist:
                    return Response({"error": "Movie not found in watchlist."}, status=status.HTTP_404_NOT_FOUND)
        elif media_type == 'tv':
            tv_show = TVShow.objects.filter(tmdb_id=media_id).first()
            if tv_show:
                try:
                    watchlist_item = WatchList.objects.get(user=user, tv_show=tv_show)
                    watchlist_item.delete()
                    return Response({"message": "TV show removed from watchlist."}, status=status.HTTP_200_OK)
                except WatchList.DoesNotExist:
                    return Response({"error": "TV show not found in watchlist."}, status=status.HTTP_404_NOT_FOUND)

        return Response({"error": "Media not found."}, status=status.HTTP_404_NOT_FOUND)
