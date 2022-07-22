from django.db import models
from django.contrib.auth.models import User

class Testimonial(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)
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