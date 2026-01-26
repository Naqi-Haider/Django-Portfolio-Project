from django.db import models

class Education(models.Model):
    """Education/Academic qualifications"""
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_year = models.CharField(max_length=20)
    end_year = models.CharField(max_length=20, blank=True, default="Present")
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0, help_text="Display order (lower first)")
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Education"
