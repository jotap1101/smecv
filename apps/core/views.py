from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
def home_view(request):
    context = {
        'user': request.user,
    }

    return render(request, 'pages/core/home.html', context)