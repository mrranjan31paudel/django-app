from django.shortcuts import render

# Create your views here.


def about_page(request):
    context = {
        'page': 'about'
    }
    return render(request, 'about.html', context)
