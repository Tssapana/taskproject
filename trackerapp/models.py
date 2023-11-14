from django.db import models

from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils import timezone



# Create your models here.






# Status Choices Tuple
STATUS_CHOICES = (
    ('To Do', 'To Do'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
)

def validate_due_date(value):
    if value < timezone.now().date():
        raise ValidationError('Due date must be in the future.')

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField(validators=[validate_due_date])
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='To Do')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})