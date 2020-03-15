from django.db import models

# Create your models here.

class Presentation(models.Model):

    nom = models.CharField(max_length=225)
    description = models.TextField(max_length=225)
    image = models.ImageField()
    video = models.TextField()

    date_add = models.DateTimeField(auto_now_add = True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)


    class Meta:
        verbose_name = 'presentation'
        verbose_name_plural ='presentations'

    def __str__(self):
        return self.nom

class Categorie(models.Model):

    nom = models.CharField(max_length=225)
    description = models.TextField(max_length=225)
    image =models.ImageField()


    date_add = models.DateTimeField(auto_now_add = True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)


    class Meta:
        verbose_name = 'categorie'
        verbose_name_plural ='categories'

    def __str__(self):
        return self.nom



class Facturation(models.Model):

    nom_categorie = models.ForeignKey(Categorie, on_delete = models.CASCADE, related_name='nom_article')
    description =models.TextField(max_length=225)
    image =models.ImageField()
    prix = models.FloatField()


    date_add = models.DateTimeField(auto_now_add = True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)


    class Meta:
        verbose_name = 'facturation'
        verbose_name_plural ='facturations'

    def __str__(self):
        return self.prix