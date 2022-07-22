from django.shortcuts import render
from .models import Testimonial

def index(request):
    testimonials = Testimonial.objects.all()
    context = {
        'testimonials': testimonials
    }
    return render(request, 'app/index.html', context)