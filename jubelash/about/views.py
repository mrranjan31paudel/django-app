from django.shortcuts import render

from about.models import Contributor

# Create your views here.


def about_page(request):
    contributor = Contributor()
    contributors = contributor.get_all_contributors()

    context = {
        'page': 'about',
        'contributors': contributors,
        'total_contributors': len(contributors)
    }
    return render(request, 'about.html', context)
