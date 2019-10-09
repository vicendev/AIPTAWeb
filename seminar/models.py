from django.db import models

# Create your models here.
class Seminar(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(upload_to="seminario", verbose_name="Imagen", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha edición")

    class Meta:
        verbose_name = "seminario"
        verbose_name_plural = "seminarios"
        ordering = ["-created"]

    def __str__(self):
        return self.title