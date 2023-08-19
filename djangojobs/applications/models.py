from django.db import models
from jobs.models import Job
from django.contrib.auth import get_user_model

User = get_user_model()

class Application(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='applications')
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    cv = models.FileField(upload_to='cvs', blank=True, null=True)
    cover_letter = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.name