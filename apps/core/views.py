from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
def home_view(request):
    context = {
        'user': request.user,
    }

    return render(request, 'pages/site/home.html', context)

# def custom_bad_request(request, exception):
#     return render(request, 'pages/errors/400.html', status=400)

# def custom_403_view(request, exception):
#     return render(request, 'pages/errors/403.html', status=403)

# def custom_404_view(request, exception):
#     return render(request, 'pages/errors/404.html', status=404)

# def custom_500_view(request):
#     return render(request, 'pages/errors/500.html', status=500)