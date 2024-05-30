from django.db import models

class Upload(models.Model):
    file_name = models.CharField(max_length=255)
    validation_result = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
