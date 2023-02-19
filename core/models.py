from django.db import models

# Create your models here.

class Precio(models.Model):
    name_vps = models.CharField(max_length=10)
    cpu = models.DecimalField(max_digits=10, decimal_places=2)
    ram = models.DecimalField(max_digits=10, decimal_places=2)
    hdd = models.DecimalField(max_digits=10, decimal_places=2)
    
    #Limites de recursos
    cpu_limit = models.IntegerField(verbose_name="Limite de CPU", help_text="Cantidad", default=1)
    ram_limit = models.IntegerField(verbose_name="Limite de RAM", help_text="en GB", default=1)
    hdd_limit = models.IntegerField(verbose_name="Limite de HDD", help_text="en GB", default=1)

    class Meta:
        verbose_name = 'Precio Recursos VPS'

    def __str__(self):
        return self.name_vps