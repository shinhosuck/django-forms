from django.contrib.auth.models import User
from django.db import models



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="profile-images")
    email = models.EmailField()
    

    def __str__(self):
        return f"{self.user} profile"