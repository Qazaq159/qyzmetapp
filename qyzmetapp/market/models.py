from django.contrib.auth.models import AbstractUser
from django.db import models


class UserInstance(AbstractUser):
    ROLE_CUSTOMER = 'CUSTOMER'
    ROLE_DEVELOPER = 'DEVELOPER'
    ROLE_CHOICES = (
        (ROLE_DEVELOPER, 'developer'),
        (ROLE_CUSTOMER, 'customer'),
    )

    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, default=ROLE_CUSTOMER)
    username = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

    def __str__(self):
        return f'<User ({self.pk}) {self.email}>'
