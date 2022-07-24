from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Accounts(AbstractUser):
   
    first_name=models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField("email", unique=True)
    email_varify = models.BooleanField(default=False)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    mobile_varify =  models.BooleanField(default=False)
    roll_id=models.IntegerField(default=1)
    photo=models.TextField(blank=True, null=True)
    username=None

    USERNAME_FIELD = "email" # make the user log in with the email
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

class ForgetPassword(models.Model):
    accounts=models.OneToOneField(Accounts,on_delete=models.CASCADE)
    token=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)