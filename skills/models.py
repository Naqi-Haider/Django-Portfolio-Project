from django.db import models

class Skill(models.Model):
    """Technical and professional skills"""
    CATEGORY_CHOICES = [
        ('programming', 'Programming Languages'),
        ('frameworks', 'Frameworks & Libraries'),
        ('tools', 'Tools & Technologies'),
        ('soft', 'Soft Skills'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, help_text="Brief description of proficiency")
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['category', 'name']
