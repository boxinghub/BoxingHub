from django.shortcuts import render
from main.utils import get_likes_and_loves

# Create your views here.
def my_affirmations(request):
    likes, loves = get_likes_and_loves()
    context = {
        'likes': likes,
        'loves': loves,
        'active': 'ai-boxing',
    }
    return render(request, 'aws_llms.html', context=context)