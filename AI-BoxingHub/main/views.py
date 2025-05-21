from django.shortcuts import render
from django.http import JsonResponse
from main.utils import get_likes_and_loves

def index(request):
    likes, loves = get_likes_and_loves()
    context = {
        'likes': likes,
        'loves': loves,
        'active': 'index',
    }
    return render(request, 'index.html', context)

def clubs(request):
    likes, loves = get_likes_and_loves()
    context = {
        'likes': likes,
        'loves': loves,
        'active': 'clubs & extra',
    }
    return render(request, 'clubs.html', context)

def fundamentals(request):
    likes, loves = get_likes_and_loves()
    context = {
        'likes': likes,
        'loves': loves,
        'active': 'knowledge',
    }
    return render(request, 'fundamentals.html', context)

def gears(request):
    likes, loves = get_likes_and_loves()
    context = {
        'likes': likes,
        'loves': loves,
        'active': 'knowledge',
    }
    return render(request, 'gears.html', context)

def moments(request):
    likes, loves = get_likes_and_loves()
    context = {
        'likes': likes,
        'loves': loves,
        'active': 'clubs & extra',
    }
    return render(request, 'moments.html', context)

def recovery(request):
    likes, loves = get_likes_and_loves()
    context = {
        'likes': likes,
        'loves': loves,
        'active': 'knowledge',
    }
    return render(request, 'recovery.html', context)

def rules(request):
    likes, loves = get_likes_and_loves()
    context = {
        'likes': likes,
        'loves': loves,
        'active': 'knowledge',
    }
    return render(request, 'rules.html', context)
