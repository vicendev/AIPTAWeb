from django.db import models

# Create your models here.
class Subscription(models.Model):
    name = models.CharField(verbose_name="nombre", max_length=50)
    email = models.EmailField(verbose_name="email", max_length=150)
    phone = models.PositiveIntegerField()
    created = models.DateField(auto_now=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Suscripción"
        verbose_name_plural = "Suscripciones"
        ordering = ["-created"]

    def __str__(self):
        return self.name