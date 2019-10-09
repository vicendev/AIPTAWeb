from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Home(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha edición")

    class Meta:
        verbose_name = "inicio"
        verbose_name_plural = "inicio"
        
    def __str__(self):
        return self.title