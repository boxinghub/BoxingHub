from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from inference_sdk import InferenceHTTPClient
import os
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO
from chatbot.views import chatbot_view
from main.models import BoxingHub  # Import from the main app

# Load environment variables from .env file
load_dotenv()
roboflow_api = os.getenv("ROBOFLOW_API")

# Initialize the client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key=roboflow_api
)

def get_likes_and_loves():
    boxinghub = BoxingHub.objects.all().first()
    if boxinghub:
        return boxinghub.likes, boxinghub.loves
    return 0, 0

@csrf_exempt
def computer_vision(request):
    if request.method == 'POST' and 'image' in request.FILES:
        image_file = request.FILES['image']
        image = Image.open(image_file)

        # Save the image to a temporary location
        temp_image_path = 'static/images/computer-vision/temp/temp_image.jpg'
        image.save(temp_image_path)

        # Perform inference
        result = CLIENT.infer(temp_image_path, model_id="boxinghub/2")

        # Draw boxes around detected objects
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("Arial.ttf", 20)

        for prediction in result["predictions"]:
            x, y = prediction['x'], prediction['y']
            width, height = prediction['width'], prediction['height']

            left, top = x - width / 2, y - height / 2
            right, bottom = x + width / 2, y + height / 2

            draw.rectangle([left, top, right, bottom], outline="blue", width=2)
            label = f" {prediction['class']} ({prediction['confidence']:.2f})"

            text_bbox = draw.textbbox((left, top), label, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]

            draw.rectangle([left, bottom, left + text_width, bottom + text_height + 2], fill="blue")
            draw.text((left, bottom), label, fill="white", font=font)

            confidence = round(prediction['confidence'], 2)
            # print(f"Detected: '{prediction['class']}' with confidence: {prediction['confidence']:.2f}")

        output_image_path = "static/images/computer-vision/classified_image.jpg"
        image.save(output_image_path)

        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        return JsonResponse({'status': 'success',
                             "classified_image": img_str,
                             "prediction": prediction['class'],
                             "confidence": confidence,
                            })
    
    elif request.method == 'POST' and 'user_input' in request.POST:
        return chatbot_view(request)

    likes, loves = get_likes_and_loves()
    context = {
        'likes': likes,
        'loves': loves,
        'active': 'ai-boxing',
    }
    return render(request, 'computer-vision.html', context)
