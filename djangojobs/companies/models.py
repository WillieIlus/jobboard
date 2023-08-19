
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify

from locations.models import Location

User = settings.AUTH_USER_MODEL

class Company(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    logo = models.ImageField(upload_to='companies/images/', blank=True, null=True)

    email = models.EmailField(max_length=200, blank=True, null=True)
    facebook = models.CharField(max_length=200, blank=True, null=True)
    twitter = models.CharField(max_length=200, blank=True, null=True)
    instagram = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Companies"
        ordering = ['name']


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Company, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('companies:detail', kwargs={'slug': self.slug})
    