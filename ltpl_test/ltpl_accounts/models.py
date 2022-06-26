from email.mime import image
from ltpl_accounts.manager import UserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    image = models.ImageField(upload_to ='profile-img')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = 'email'

roles = (
    ("teacher","Teacher"),
    ("student","Student"),
    ("staff","Staff"),

)

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    location = models.CharField(max_length=500)
    date_of_birth = models.DateTimeField(null=True)
    role = models.CharField(choices=roles,max_length=50,default="student")