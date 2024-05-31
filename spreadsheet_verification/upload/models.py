# models.py
from django.db import models

class Upload(models.Model):
    file = models.FileField(upload_to='uploads/')
    file_name = models.CharField(max_length=255)
    validation_result = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=False)  # New field to indicate validation status

    def __str__(self):
        return self.file_name
