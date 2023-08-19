from django.db import models
from django.urls import reverse

from django.utils.text import slugify


# Create your Country and Location models here.

class Country(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    code = models.CharField(max_length=200, blank=True, null=True)
    flag = models.ImageField(upload_to='countries/flags/', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Countries"
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)

class Location(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    flag = models.ImageField(upload_to='locations/flags/', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Locations"
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Location, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('location:detail', kwargs={'slug': self.slug})
    
    