from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):

    def __self__(self):
        return "@{}".fromat(self.username)
