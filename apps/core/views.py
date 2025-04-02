from django.shortcuts import render

# Create your views here.
def home_view(request):
    context = {
        'user': request.user,
    }

    return render(request, 'pages/home.html', context)