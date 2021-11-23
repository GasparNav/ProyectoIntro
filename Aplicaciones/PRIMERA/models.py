from django.db import models

# Create your models here.

class material(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    calificacion = models.IntegerField()
    fecha_subida = models.DateField()
    etiquetas = models.TextField()
    tipo = models.TextField()
    archivo = models.FileField(null=True)

    def __str__(self):
        return self.titulo  




