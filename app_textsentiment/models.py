from django.db import models
from django.contrib.auth.models import User
import requests

# Create your models here.
class CSVFile(models.Model):
    file = models.FileField(upload_to='csv_files/')

    
class Text(models.Model):
    csv_file = models.ForeignKey(CSVFile, on_delete=models.CASCADE)
    text_content = models.TextField()

class APIResponse(models.Model):
    result_key = models.CharField(max_length=255)
    result_value = models.TextField()

    def __str__(self):
        return f"{self.result_key}: {self.result_value}"