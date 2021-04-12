from django.shortcuts import render

from home.models import HomeModel

# Create your views here.


def home_dashboard(request):
    home_model = HomeModel()
    context = {
        'page': 'home',
        'time': home_model.get_display_time_now()
    }
    return render(request, 'home.html', context)
