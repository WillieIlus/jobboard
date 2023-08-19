from datetime import datetime, timedelta, date
from decimal import Decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from locations.models import Location
from categories.models import Category
from companies.models import Company
from plans.models import Plan

User = settings.AUTH_USER_MODEL


class Job(models.Model):
    JOB_TYPE = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Freelance', 'Freelance'),
        ('Internship', 'Internship'),
        ('Temporary', 'Temporary'),
        ('Contract', 'Contract'),
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='jobs/', blank=True)
    author = models.ForeignKey(
        User, related_name='author', on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, blank=True)
    requirements = models.TextField(max_length=1000, blank=True)
    salary = models.IntegerField(default=0, validators=[
                                 MinValueValidator(0), MaxValueValidator(100000)])
    experience = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    openings = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    work_hours = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default=1)
    is_published = models.BooleanField(default=False)
    applicant = models.ManyToManyField(
        User, related_name='applicants', blank=True)
    url=models.URLField(max_length=200, blank=True, help_text="Enter the URL of the job posting")


    active = models.BooleanField(default=True)
    views_count = models.IntegerField(default=0)
    click_count = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    paid_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal('0.00'))
    paid_at = models.DateTimeField(blank=True, null=True)
    paid_until = models.DateTimeField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Jobs'

    def __str__(self):
        return self.title + ' - ' + self.company.name

    def get_absolute_url(self):
        return reverse('jobs:detail', kwargs={'slug': self.slug})
    
    def get_job_type(self):
        return self.job_type

    def save(self, *args, **kwargs):
        slug_str = '%s %s %s' % (
            self.title, self.company.name, self.location.name)
        self.slug = slugify(slug_str)
        super(Job, self).save(*args, **kwargs)

    def get_job_applicants(self):
        return self.applicant.all()

    @classmethod
    def get_active_jobs(cls):
        return cls.objects.filter(active=True)

    @classmethod
    def is_featured(cls):
        return cls.objects.filter(featured=True)

    @classmethod
    def is_paid(cls):
        return cls.objects.filter(paid=True)

    @classmethod
    def is_active(cls):
        return cls.objects.filter(active=True)
    
    def timeSince(self):
        return self.created_at.strftime("%b %d %Y %H:%M:%S")
    
    def days_left(self):
        pass
    
    def expires_soon(self):
        pass
    
    def is_expired(self):
        pass



class Impression(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    source_ip = models.GenericIPAddressField(null=True, blank=True)
    session_id = models.CharField(max_length=50, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Impressions'
        # indexed_together = ('job', 'session_id',)

    def __str__(self):
        return self.job.title

    def get_impressions(self):
        return self.impressions.all()


class Click(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    source_ip = models.GenericIPAddressField(null=True, blank=True)
    session_id = models.CharField(max_length=50, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Clicks'
        # indexed_together = ('job', 'session_id',)

    def __str__(self):
        return self.job.title

    def get_clicks(self):
        return self.clicks.all()
