from django.shortcuts import render
from django.http import JsonResponse
from .models import BoxingHub
# from computer_vision.views import computer_vision


def get_likes_and_loves():
    boxinghub = BoxingHub.objects.all().first()
    if boxinghub:
        return boxinghub.likes, boxinghub.loves
    return 0, 0

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

def update_like(request):
    if request.method == 'POST':
        new_like = request.POST.get('like')  # Assuming 'like' is sent via AJAX
        boxinghub = BoxingHub.objects.first()
        if boxinghub:
            boxinghub.likes = new_like
            boxinghub.save()
        else:
            BoxingHub.objects.create(likes=new_like, loves=0)
        return JsonResponse({"message": "Like updated successfully"})
    return JsonResponse({'status': 'error'}, status=400)

def update_love(request):
    if request.method == 'POST':
        new_love = request.POST.get('love')  # Assuming 'love' is sent via AJAX
        boxinghub = BoxingHub.objects.first()
        if boxinghub:
            boxinghub.loves = new_love
            boxinghub.save()
        else:
            BoxingHub.objects.create(likes=0, loves=new_love)
        return JsonResponse({"message": "Love updated successfully"})
    return JsonResponse({'status': 'error'}, status=400)

# ----------------------------
# Computer Vision API
# from computer_vision.views import computer_vision

# ----------------------------
# Accessibility API
def accessibility(request):
    likes, loves = get_likes_and_loves()
    context = {
        'likes': likes,
        'loves': loves,
        'active': 'ai-boxing',
    }
    return render(request, 'accessibility.html', context)