from django.db import models
from django.conf import settings
from django.utils import timezone

class Note(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    last_edited_date = models.DateTimeField(default = timezone.now)

    def update_last_edited_date(self):
        self.last_edited_date = timezone.now

    def __str__(self):
        return self.title