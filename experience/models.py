from django.db import models

class Experience(models.Model):
    """Professional and academic experience"""
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    experience_type = models.CharField(max_length=50, choices=[
        ('professional', 'Professional'),
        ('academic', 'Academic'),
        ('internship', 'Internship'),
    ], default='academic')
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, blank=True, default="Present")
    description = models.TextField()
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.title} at {self.organization}"
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Experience"
