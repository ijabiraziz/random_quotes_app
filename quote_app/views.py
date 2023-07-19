import requests
from .models import Quote
from django.shortcuts import render


def fetch_quotes():
    api_url = "https://type.fit/api/quotes"
    response = requests.get(api_url).json()
    for quote in response:
        Quote.objects.create(text=quote["text"], author=quote["author"])


def home(request):
    fetch_quotes()
    quotes = Quote.objects.order_by("?")[:2]
    return render(request, "quote_app/home.html", {"quotes": quotes})
