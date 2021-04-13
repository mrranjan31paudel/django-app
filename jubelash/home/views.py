from django.shortcuts import render

from datetime import datetime

# Create your views here.


def home_dashboard(request):
    context = {
        'page': 'home',
        'time': datetime.now().strftime('%A, %B %d %Y, %I:%M:%S %p')
    }
    return render(request, 'home.html', context)
