from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=50, blank=True)
    skills = models.JSONField(default=list)
    experience = models.CharField(max_length=50, blank=True)
    posted = models.CharField(max_length=50, blank=True)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.company}"
