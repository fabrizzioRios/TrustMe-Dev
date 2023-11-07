from django.db import models
from django.contrib.auth.models import AbstractUser


class Opinion(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=350, blank=True, null=True)
    rating = models.IntegerField(default=0, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    page_id = models.ForeignKey("trustme_test.Page", on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey("trustme_test.User", on_delete=models.DO_NOTHING, blank=True, null=True)


class Page(models.Model):
    url = models.CharField(max_length=100, blank=True, null=True, unique=True)
    page_name = models.CharField(max_length=30, blank=True, null=True, unique=True)
    name_servers = models.CharField(max_length=100, blank=True, null=True)
    registrar = models.CharField(max_length=100, blank=True, null=True)
    registrant_name = models.CharField(max_length=100, blank=True, null=True)
    registrant_city = models.CharField(max_length=80, blank=True, null=True)
    registrant_state = models.CharField(max_length=80, blank=True, null=True)
    registrant_country = models.CharField(max_length=80, blank=True, null=True)
    admin = models.CharField(max_length=100, blank=True, null=True)
    admin_city = models.CharField(max_length=80, blank=True, null=True)
    admin_country = models.CharField(max_length=80, blank=True, null=True)
    admin_state = models.CharField(max_length=80, blank=True, null=True)
    tech_name = models.CharField(max_length=80, blank=True, null=True)
    tech_city = models.CharField(max_length=80, blank=True, null=True)
    tech_state = models.CharField(max_length=80, blank=True, null=True)
    tech_country = models.CharField(max_length=80, blank=True, null=True)
    biling_name = models.CharField(max_length=80, blank=True, null=True)
    biling_city = models.CharField(max_length=80, blank=True, null=True)
    biling_state = models.CharField(max_length=80, blank=True, null=True)
    domain_name = models.CharField(max_length=100, blank=True, null=True, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    expiration_date = models.DateField(blank=True, null=True)
    status = models.BooleanField(default=False)
    created_by = models.ForeignKey("trustme_test.User", blank=True, null=True, related_name="pages",
                                   on_delete=models.DO_NOTHING)


class User(AbstractUser):
    rfc = models.CharField(max_length=14, blank=True, null=True)
