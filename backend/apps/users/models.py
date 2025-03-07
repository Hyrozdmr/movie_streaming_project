# apps/users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from apps.movies.models import Movie, TVShow
from django.contrib.auth import get_user_model

class UserManager(BaseUserManager):
    """Custom manager for the User model."""
    
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    """Custom User model."""
    
    email = models.EmailField(unique=True)
    objects = UserManager()

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username


# Now you can use get_user_model() to refer to the custom User model in other models
User = get_user_model()

class WatchList(models.Model):
    user = models.ForeignKey(User, related_name="watchlist", on_delete=models.CASCADE)
    media_type = models.CharField(max_length=50, choices=[('movie', 'Movie'), ('tv', 'TVShow')])
    movie = models.ForeignKey(Movie, related_name="watchlists", null=True, blank=True, on_delete=models.CASCADE)
    tv_show = models.ForeignKey(TVShow, related_name="watchlists", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.media_type}"
