from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """User profile manager"""

    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
                raise ValueError('User must have email address')

        email = self.normalize_email(email)
        user = self.model(email=email,name=name)

        user.set_password(password) #Hashing password
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    '''DB models for users'''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retreive fullname"""
        return self.name

    def get_short_name(self):
        """Retreive short name"""
        return self.name

    def __str__(self):
        return self.email
