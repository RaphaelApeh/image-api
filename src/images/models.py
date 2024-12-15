from django.db import models
from django.conf import settings 
from django.utils import crypto, text

from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField

from .utils import convert_from_bytes, cloudinary_init

User = settings.AUTH_USER_MODEL

cloudinary_init()

class Image(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=20)
    tags = TaggableManager()
    image = CloudinaryField("image")
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    active = models.BooleanField(default=True)
    
    def __str__(self)-> str:
        return self.name
    
    def save(self, **kwargs):
        
        if self.name is not None:
            name = self.name
        else:
            name = crypto.get_random_string(12)
        
        if self.slug is None or "":
            self.slug = text.slugify(name)
        
        super().save(**kwargs)

    def build_image_url(self, width=300, **kwargs):
        kwargs['width'] = width
        image_url = self.image.build_url(**kwargs)
        return image_url
    
    def get_image_url(self):
        image = self.image.url

        return image