from email.mime import image
from importlib.resources import path
from pydoc import describe
from django.db import models

from pathlib import Path
from django.templatetags.static import static
from datetime import datetime
from django.utils.text import slugify
from django.dispatch import receiver
from django.conf import settings 
import boto3   
from django.contrib.admin import ModelAdmin
from PIL import Image
from io import BytesIO
from django.core.files import File
from django_resized import ResizedImageField
from django.utils.html import mark_safe
from django.utils.html import format_html
# Create your models here.

class Publication(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    link_to = models.URLField(max_length=200, blank=True, null=True)
    link_str = models.CharField(max_length=200, blank=True,null=True)
    date_published = models.DateField(default=datetime.now)
    published  = models.BooleanField(default=True)
    
    def __str__(self):
        return (f"{self.title} - {self.description} - {self.link_to} - {self.link_str} - {self.date_published} - {self.published}")
    def __repr__(self):
        return self.title

class PublicationImage(models.Model):
    publication = models.ForeignKey("Publication",related_name='photos', on_delete=models.CASCADE , blank=True, null=True)
    photo_url = models.ImageField(upload_to='publication_images/')
    
    @property
    def get_photo_url(self):
        p = Path(self.photo_url.path) 
        path = (p.parts[-3]+'/'+p.parts[-2] +'/'+ p.name)
        return static(path)

    def delete(self):
        s3 = boto3.client('s3')
        s3.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=f"media/{self.photo_url.path}")
        super().delete()
        return  super().delete()


class Contact(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    sujet = models.CharField(max_length=255 , blank=True, null=True)
    message = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __repr__(self):
        return self.nom

    def __str__(self):
        return self.nom


class Livre(models.Model):
    nom = models.CharField(max_length=255)
    message = models.TextField()
    date_update = models.DateTimeField(default=datetime.now())
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'livre d\'or'
        verbose_name_plural = 'livre d\'or'
    
    def __repr__(self):
        return self.nom

    def __str__(self):
        return self.nom


class PresentationCard(models.Model):
    titre = models.CharField(max_length=50)
    card_image = models.CharField(max_length=255)
    card_description = models.TextField()
    
    class Meta:
        verbose_name = 'PrésentationCard'
        verbose_name_plural = 'PrésentationCards'
    
    def get_photo_url(self):
        p = self.card_image
        return static(p)

    def __repr__(self):
        return self.card_description

class Presentation(models.Model):
    description_one = models.TextField(blank=True, null=True)
    description_two = models.TextField(blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Presentation'
        verbose_name_plural = 'Presentations'
    
    def __repr__(self):
        return self.description_one
    


class Galeries(models.Model):
    titre = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)
    background_photo = models.ImageField(upload_to='galeries_images/', blank=True, null=True)
    class Meta:
        verbose_name = 'Galerie'
        verbose_name_plural = 'Galeries'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super().save(*args, **kwargs)
    
    @property
    def get_background_photo_url(self):
        p = Path(self.background_photo.path) 
        path = (p.parts[-3]+'/'+p.parts[-2] +'/'+ p.name)
        return static(path)
    
    def image_tag(self):
        from django.utils.html import escape
        return format_html( u'<img src="%s" height="80" />' % escape(self.background_photo.url))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class GaleriesImage(models.Model):
    galeries = models.ForeignKey("Galeries",related_name='photos', on_delete=models.CASCADE , blank=True, null=True)
    photo = ResizedImageField(size=[None, 500],upload_to='galeries_images/', blank=True, null=True)
    

    # before saving the instance we’re reducing the image
    def save(self, *args, **kwargs):
        new_image = self.reduce_image_size(self.photo)
        self.photo = new_image
        super().save(*args, **kwargs)
    def reduce_image_size(self, photo):
        img = Image.open(photo)
        thumb_io = BytesIO()
        img.save(thumb_io, 'jpeg', quality=50)
        new_image = File(thumb_io, name=photo.name)
        return new_image

    @property
    def get_photo_url(self):
        p = Path(self.photo.path) 
        path = (p.parts[-3]+'/'+p.parts[-2] +'/'+ p.name)
        return static(path)

    def image_tag(self):
        from django.utils.html import escape
        return format_html( u'<img src="%s" height="80" />' % escape(self.photo.url))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


    
@receiver(models.signals.post_delete, sender=GaleriesImage)
def remove_file_from_s3(sender, instance, using, **kwargs):
    instance.photo.delete(save=False)    
    