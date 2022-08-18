from django.views.decorators.cache import cache_page  
from django.shortcuts import render
from .models import Testimonial


@cache_page(60 * 1000)
def index(request):
    testimonials = Testimonial.objects.all()
    context = {
        'testimonials': testimonials
    }
    return render(request, 'app/index.html', context)