from django.db import models

class Profile(models.Model):
    """Single row for bio/hero section"""
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"


class Education(models.Model):
    """Education entries"""
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    date_range = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.title} - {self.institution}"
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Education"


class Skill(models.Model):
    """Skills with categories"""
    CATEGORY_CHOICES = [
        ('programming', 'Programming Languages'),
        ('frameworks', 'Frameworks & Libraries'),
        ('tools', 'Tools & Technologies'),
        ('soft', 'Soft Skills'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['category', 'name']


class Experience(models.Model):
    """Experience and projects"""
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    date = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Experience"
