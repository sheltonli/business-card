from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):

    email           = models.CharField(max_length=254, unique=True)

    full_name       = models.CharField(max_length=100)
    address         = models.CharField(max_length=150)
    address_2       = models.CharField(max_length=150, blank=True)
    city            = models.CharField(max_length=100)
    country         = models.CharField(max_length=100)
    province_state  = models.CharField(max_length=100)
    postal_code     = models.CharField(max_length=20)
    phone_number    = models.CharField(max_length=20)

    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)

    created_on      = models.DateTimeField(auto_now_add=True)
    updated_on      = models.DateTimeField(auto_now=True)

    @property
    def username(self):
        # required for displaying username in admin interface
        return self.get_username()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'user'
        app_label = 'business_card'
        managed = True

    def __str__(self):
        return self.email
