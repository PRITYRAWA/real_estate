from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from .managers import UserManager

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    createdby = models.CharField(max_length=36, blank=True, null=True)
    lastmodifiedby = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        abstract = True

class CustomUser(AbstractUser,PermissionsMixin):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    objects = UserManager()

    def __str__(self) -> str:
        return self.email
    
