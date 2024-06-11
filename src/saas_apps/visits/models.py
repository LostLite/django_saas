from django.db import models

# Create your models here.
class PageVisit(models.Model):
    
    """
    Class to store stats on page visits
    
    path is the url accessed by the site visitor
    timestamp is the time the visitor accessed page
    """
    
    path = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    