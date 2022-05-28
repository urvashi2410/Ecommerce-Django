from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, username, password=None):
        """
        Creates and saves a User with the given email, first_name, last_name, username and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email       = self.normalize_email(email),
            first_name  = first_name,
            last_name   = last_name,
            username    = username 
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, username, password=None):
        """
        Creates and saves a superuser with the given email, first_name, last_name, username and password.
        """
        user = self.create_user(
            email       = self.normalize_email(email),
            first_name  = first_name,
            last_name   = last_name,
            username    = username,
            password    = password,
        )
        user.is_admin       = True
        user.is_active      = True 
        user.is_staff       = True 
        user.is_superadmin  = True 
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.CharField(max_length=50)

    #required 
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=False)
    is_superadmin   = models.BooleanField(default=False)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects         = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
