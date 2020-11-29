from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('published','Published')       
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    published = models.DateField(default=timezone.now)
    created = models.DateField(auto_now_add=True)
    edited = models.DateField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='draft')
    
    class Meta:
        ordering = ('published',)

    def __str__(self):
        return self.title
