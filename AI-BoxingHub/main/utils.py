from .models import BoxingHub
from django.http import JsonResponse

def get_likes_and_loves():
    boxinghub = BoxingHub.objects.all().first()
    if boxinghub:
        return boxinghub.likes, boxinghub.loves
    return 0, 0

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