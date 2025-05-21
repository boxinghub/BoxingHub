from django.http import JsonResponse
from django.shortcuts import render
from .bot import BoxingChatbot

chatbot = BoxingChatbot()

def chatbot_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        response = chatbot.get_response(user_input)
        return JsonResponse(response)
    return render(request, 'chatbot.html')
