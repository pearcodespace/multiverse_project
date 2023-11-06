from django.db import models

# Create your models here.
class ClothDescription(models.Model):
    Cloth_ID = models.IntegerField()
    Age = models.IntegerField()
    Review_Text = models.CharField(max_length=255)
    Rating = models.IntegerField()
    Positive_Feedback_Count = models.IntegerField()
    Department_Name = models.CharField(max_length=255)

# class FlipkartProduct(models.Model):
#     product_name = models.TextField()
#     product_price = models.IntegerField()
#     rate = models.IntegerField()
#     review = models.TextField()
#     summary = models.TextField()
#     sentiment = models.TextField()