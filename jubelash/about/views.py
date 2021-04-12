from django.shortcuts import render

from about.models import AboutModel

# Create your views here.


def about_page(request):
    about_model = AboutModel()
    contributors = about_model.get_contributers_list()
    context = {
        'page': 'about',
        'contributors': contributors,
        'total_contributors': len(contributors)
    }
    return render(request, 'about.html', context)
