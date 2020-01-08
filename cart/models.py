from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Feature(models.Model):
    """
    Creates a single bug report in the database
    """
    Done = 'Done'
    Doing = 'Doing'
    ToDo = 'ToDo'
    FIX_STATUS_CHOICES = [
        (Done, 'Done'),
        (Doing, 'Doing'),
        (ToDo, 'ToDo'),
        ]

    title = models.CharField(max_length=100)
    details = models.TextField()
    fix_status = models.CharField(
                                  max_length=6,
                                  choices=FIX_STATUS_CHOICES,
                                  default='ToDo'
                                )
    posted_on = models.DateTimeField(
                                     null=True,
                                     blank=True,
                                     default=timezone.now
                                    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title