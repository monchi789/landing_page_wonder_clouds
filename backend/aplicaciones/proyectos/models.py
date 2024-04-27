from django.db import models

# Create your models here.
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Proyectos(models.Model):
    titulo = models.CharField(max_length=50, blank=False, null=False, default='')
    descripcion = models.CharField(max_length=250, blank=False, null=False, default='')
    link = models.CharField(max_length=250, blank=False, null=False, default='')
    image = models.ImageField(upload_to=upload_to, blank=False, null=False, default='')

    def __str__(self):
        return f'{self.titulo} - {self.link}'
