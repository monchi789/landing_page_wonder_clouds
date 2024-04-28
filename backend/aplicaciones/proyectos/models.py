from django.db import models

def upload_to(instance, filename):
    """
    Devuelve la ruta de almacenamiento para un archivo cargado.

    Args:
        instance: La instancia del modelo que está siendo guardada.
        filename: El nombre del archivo original.

    Returns:
        La ruta de almacenamiento para el archivo cargado.
    """
    return 'images/{filename}'.format(filename=filename)


class Proyectos(models.Model):
    """
    Modelo que representa un proyecto.

    Atributos:
        titulo (str): El título del proyecto.
        descripcion (str): La descripción del proyecto.
        link (str): El enlace del proyecto.
        image (ImageField): La imagen asociada al proyecto.

    Métodos:
        __str__(): Devuelve una representación legible en cadena del objeto Proyectos.
    """
    titulo = models.CharField(max_length=50, blank=False, null=False, default='')
    descripcion = models.CharField(max_length=250, blank=False, null=False, default='')
    link = models.CharField(max_length=250, blank=False, null=False, default='')
    image = models.ImageField(upload_to=upload_to, blank=False, null=False, default='')

    def __str__(self):
        return f'{self.titulo} - {self.link}'
