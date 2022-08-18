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


@cache_page(60 * 1000)
def error_403_view(request, exception):
    context = {
        'is_active': '403'
    }
    return render(request, 'app/handler/page-403.html', context)

@cache_page(60 * 1000)
def error_404_view(request, exception):
    context = {
        'is_active': '404'
    }
    return render(request, 'app/handler/page-404.html', context)



@cache_page(60 * 1000)
def error_500_view(request):
    context = {
        'is_active': '500'
    }
    return render(request, 'app/handler/page-500.html', context)
