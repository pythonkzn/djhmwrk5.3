import time
import random
import requests

from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


def ticket_page_view(request):
    template = 'app/ticket_page.html'

    context = {
        'form': SearchTicket()
    }

    return render(request, template, context)


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    city_look_for = request.GET.get('term')
    cache_key = city_look_for.lower().replace(' ', '_')
    results = cache.get(cache_key)

    if results is None:
        results = []
        cities = City.objects.all()
        for city in cities:
            if city_look_for in city.name:
                results.append(city.name)
        cache.set(cache_key, results)

    return JsonResponse(results, safe=False)
