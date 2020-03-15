from django.contrib import admin
from .import models
# Register your models here.
admin.site.register(models.Presentation),
admin.site.register(models.Categorie),
admin.site.register(models.Facturation)