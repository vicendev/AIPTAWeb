from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200 ,verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha edición")

    class Meta:
        verbose_name = "nosotros"
        verbose_name_plural = "somos"

    def __str__(self):
        return self.title