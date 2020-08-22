from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
class Setting(models.Model):
    STATUS =(
        ('True', 'Mavjud'),
        ('False', 'Mavjud emas'),
    )
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = RichTextField()
    address = models.CharField(max_length=255)
    phone = models.IntegerField()
    fax = models.IntegerField()
    email = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    facebook = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255)
    aboutus = RichTextField()
    contacts = RichTextField()
    status = models.CharField(max_length=15, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

