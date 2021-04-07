from django.shortcuts import render

# Create your views here.


def home_dashboard(request):
    context = {
        'page': 'home'
    }
    return render(request, 'home.html', context)
