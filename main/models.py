import uuid
from django.db import models

class Product(models.Model):
    # CATEGORY_CHOICES = [
    #     ('transfer', 'Transfer'),
    #     ('update', 'Update'),
    #     ('exclusive', 'Exclusive'),
    #     ('match', 'Match'),
    #     ('rumor', 'Rumor'),
    #     ('analysis', 'Analysis'),
    # ]
    
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    @property
    def is_news_hot(self):
        return self.news_views > 20
        
    def increment_views(self):
        self.news_views += 1
        self.save()