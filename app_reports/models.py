from django.db import models

# Create your models here.
class ClothDescription(models.Model):
    Cloth_ID = models.IntegerField()
    Age = models.IntegerField()
    Review_Text = models.CharField(max_length=255)
    Rating = models.IntegerField()
    Department_Name = models.CharField(max_length=255)
