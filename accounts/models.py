from uuid import uuid4
from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, password):
        if not email:
            raise ValueError("Email is Required.")
        user = self.model(email=email)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.model(email=email, date_joined=timezone.now())
        user.set_password(password)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    """ User Model """

    objects = UserManager()

    uuid = models.UUIDField(primary_key=True, default=uuid4)
    email = models.EmailField(max_length=254, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ["username"]
