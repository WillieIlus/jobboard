from django.db import models


class Plan(models.Model):
    title = models.CharField("title", unique=True, max_length=200)
    description = models.TextField("description", blank=True, null=True)
    price_per_day = models.DecimalField("price per day", max_digits=10, decimal_places=2, blank=True, null=True)
    trial_period = models.IntegerField("trial period", blank=True, null=True)
    is_default = models.BooleanField("is default", default=False)
    is_fallback = models.BooleanField("is fallback", default=False)
    is_available = models.BooleanField("is available", default=True)
    is_active = models.BooleanField("is active", default=True)
    is_featured = models.BooleanField("is featured", default=False)
    weight = models.IntegerField("weight", default=0)
    created = models.DateTimeField("created", auto_now_add=True)
    updated = models.DateTimeField("updated", auto_now=True)

    class Meta:
        verbose_name_plural = "Plans"
        ordering = ['weight']

    def __str__(self):
        return f'{self.title}: Ksh {self.price_per_day} per day'
