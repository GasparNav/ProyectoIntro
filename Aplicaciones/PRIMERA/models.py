from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating

# Create your models here.

class material(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_subida = models.DateField()
    etiquetas = models.TextField()
    tipo = models.TextField()
    archivo = models.FileField(null=True)
    ratings = GenericRelation(Rating, related_query_name='material_rating')

    def __str__(self):
        return self.titulo  

class comentario(models.Model):
    material = models.ForeignKey(material, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class calificacion(models.Model):
    material = models.ForeignKey(material, on_delete=models.CASCADE, related_name='calificacion')
    calificacion = models.FloatField()
    

    def __str__(self):
        return self.text



