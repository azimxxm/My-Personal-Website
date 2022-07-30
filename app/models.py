from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Testimonial(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)
    is_published = models.BooleanField(default=False)
    testimonial = models.TextField(max_length=400)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    customer_pic = models.ImageField(upload_to='Testimonial/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.customer_pic.path)
        if img.height > 1000 or img.width > 1000:
            # image new width and new heigth
            new_width = img.height // 2
            new_height = img.width // 2
            # resize image
            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img.save(self.customer_pic.path)

        else:
            img.save(self.customer_pic.path)