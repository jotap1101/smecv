from datetime import datetime
from django.conf import settings
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import pytz
import requests

# Create your views here.
def get_weather():
    cache_key = 'weather_data'
    weather = cache.get(cache_key)

    if weather is not None:
        return weather

    api_key = settings.OPENWEATHER['API_KEY']
    city = settings.OPENWEATHER['CITY']
    country = settings.OPENWEATHER['COUNTRY']
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric&lang=pt_br"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        weather = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': round(data['main']['temp']),
            'description': data['weather'][0]['description'].capitalize(),
            'icon': data['weather'][0]['icon']
        }

        cache.set(cache_key, weather, timeout=1800)  # 30 minutos
        return weather

    except Exception:
        return {
            'city': city,
            'country': country,
            'temperature': None,
            'description': 'Não disponível',
            'icon': '01d'
        }

def get_daily_quote():
    quotes = [
        "Acredite, você é mais forte do que pensa.",
        "A persistência realiza o impossível.",
        "Coragem é agir mesmo com medo.",
        "Cada dia é uma nova chance para recomeçar.",
        "Sonhar grande dá o mesmo trabalho que sonhar pequeno.",
        "A vida é feita de escolhas, faça as certas.",
        "A gratidão transforma o que temos em suficiente.",
        "A felicidade não é um destino, é uma forma de viajar.",
        "O sucesso é a soma de pequenos esforços repetidos dia após dia.",
        "A única maneira de fazer um ótimo trabalho é amar o que você faz.",
        "Não espere por oportunidades, crie-as.",
        "A única limitação que você tem é aquela que você impõe a si mesmo.",
    ]
    index = datetime.now().day % len(quotes)

    return quotes[index]

def home_view(request):
    now = datetime.now(pytz.timezone('America/Sao_Paulo'))
    weather = get_weather()
    quote = get_daily_quote()

    context = {
        'user': request.user,
        'datetime': now.strftime('%d/%m/%Y %H:%M'),
        'weather': weather,
        'quote': quote,
    }

    return render(request, 'pages/core/home.html', context)

@login_required
def dashboard_view(request):
    return render(request, 'pages/core/dashboard.html', {'user': request.user})