from django.db import models



class Oficina(models.Model):
    """Model definition for Oficina."""

    nombre = models.CharField('Nombre de la oficina', max_length=50)
    nombre_corto = models.CharField('Nombre corto', max_length=50)


    class Meta:
        """Meta definition for Oficina."""

        verbose_name = 'Oficina'
        verbose_name_plural = 'Oficinas'

    def __str__(self):
        """Unicode representation of Oficina."""
        return self.nombre_corto

