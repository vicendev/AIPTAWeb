from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = RichTextField()
    pdfFile = models.FileField(upload_to="documentos/%Y/%m/%d", validators=[FileExtensionValidator(allowed_extensions=['pdf','doc','docx'], message="Extensión no soportada, solo archivos pdf y word.")])
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha edición")

    class Meta:
        verbose_name = "otras publicaciones"
        verbose_name_plural = "otras publicaciones"

    def __str__(self):
        return self.title

