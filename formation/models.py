from django.db import models

# Create your models here.
class Formation(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(upload_to="formation", verbose_name="Imagen", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha edición")

    class Meta:
        verbose_name = "formación"
        verbose_name_plural = "formaciones"
        ordering = ["-created"]

    def __str__(self):
        return self.title