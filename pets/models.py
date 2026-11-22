from django.db import models
from django.conf import settings

class Pet(models.Model):
    name = models.CharField(max_length=100)
    animal_type = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class AdoptionRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('declined', 'Declined'),
    ]
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='adoption_requests')
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='adoption_requests')
    message = models.TextField(max_length=500, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.applicant} → {self.pet} ({self.status})'

# Create your models here.
