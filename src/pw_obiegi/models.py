from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.core.urlresolvers import reverse

User = settings.AUTH_USER_MODEL


class Material(models.Model): #one
    material_name               = models.CharField(max_length=50)
    producent          = models.CharField(max_length=50)
    dostawca           = models.CharField(max_length=50)
    szerokosc		   = models.DecimalField(max_digits=4, decimal_places=2)
    dlugosc     	   = models.DecimalField(max_digits=4, decimal_places=2)
    cena               = models.DecimalField(max_digits=6, decimal_places=2)
    pass
    def __str__(self):
	    return self.material_name
    
class Status(models.Model): #one
    status_name               = models.CharField(max_length=50)
    pass
    def __str__(self):
	    return self.status_name

class Obieg(models.Model): #many
    obieg_name         = models.CharField(max_length=50)
    obieg_type         = models.BooleanField(default=False)
    kod_presta         = models.CharField(max_length=50)
    material           = models.ForeignKey(Material, on_delete=models.CASCADE)
    laminacja          = models.BooleanField()
    link_podgladu      = models.URLField(max_length=200)
    zamawiajacy        = models.CharField(max_length=100)
    status			   = models.ForeignKey(Status, on_delete=models.CASCADE)
    handlowiec		   = models.ForeignKey(User, default=1)
    uwagi              = models.TextField(max_length=500, null=True)
    data_wprowadzenia  = models.DateTimeField(auto_now_add=True)
    data_edycji 	   = models.DateTimeField(auto_now=True)
    slug               = models.SlugField(null=True, blank=True)
    def __str__(self):
	    return self.obieg_name
    @property
    def title(self):
	    return self.obieg_name
    def get_absolute_url(self):
        return reverse('obiegi:detail', kwargs={'slug': self.slug})
    class Meta:
        ordering = ['-data_wprowadzenia']
	    
	    
def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    
# def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
#     print('Zapisano')
#     print(instance.data_wprowadzenia)
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#         instance.save()
    
pre_save.connect(rl_pre_save_receiver, sender=Obieg)
# post_save.connect(rl_post_save_receiver, sender=Obieg)