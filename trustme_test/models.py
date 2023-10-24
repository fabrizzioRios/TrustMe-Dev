from django.db import models


class UserModel(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    first_lastname = models.CharField(max_length=30)
    second_lastname = models.CharField(max_length=30)
    age = models.IntegerField()
    born_date = models.DateField(default=False)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return self.username

# Create your models here.
