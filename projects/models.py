from django.db import models

class Project(models.Model):
    """Personal and academic projects"""
    title = models.CharField(max_length=200)
    project_type = models.CharField(max_length=50, choices=[
        ('personal', 'Personal Project'),
        ('academic', 'Academic Project'),
        ('freelance', 'Freelance'),
    ], default='personal')
    technologies = models.CharField(max_length=200, help_text="Technologies used, comma separated")
    description = models.TextField()
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order']
