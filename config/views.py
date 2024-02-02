from django.shortcuts import render
import openai
import os
import requests
from dotenv import load_dotenv
from django.core.files.base import ContentFile
from images.models import Images
load_dotenv()

api_key = os.getenv('OPENAI_KEY', None)
openai.api_key = api_key


def generate_image_to_text(request):
    obj = None
    if api_key is not None and request.method == 'POST':
        user_input = request.POST.get('user_input')
        response = openai.Image.create(
            prompt=user_input,
            size='256x256'  # 256x256, 512x512, and 1024x1024

        )
        print("before response")
        print(response)
        img_url = response["data"][0]["url"]
        response = requests.get(img_url)
        print(response)  # <Response [200]>
        img_file = ContentFile(response.content)

        count = Images.objects.count() + 1
        fname = f"image-{count}.jpg"

        obj = Images(phrase=user_input)
        obj.ai_image.save(fname, img_file)
        obj.save()
        print("before object print")
        print(obj)

    context = dict(
        object=obj,
    )
    return render(request, "main.html", context)


def main_home(request):
    return render(request, 'base.html')
