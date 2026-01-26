from django.db import models

class Bio(models.Model):
    """Profile/Bio section - single row"""
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    description = models.TextField()
    profile_picture = models.URLField(blank=True, help_text="URL to profile picture")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Bio"
        verbose_name_plural = "Bio"
