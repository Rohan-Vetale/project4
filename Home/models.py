from django.db import models

class SearchQ(models.Model):
    query = models.CharField(max_length=15)
    created_at = models.DateField()
    
# Create your models here.
