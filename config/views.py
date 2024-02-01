from django.shortcuts import render
import openai
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('OPENAI_KEY', None)
openai.api_key = api_key


def generate_image_to_text(request):
    if api_key is not None and request.method == 'POST':
        user_input = request.POST.get('user_input')
        response = openai.Image.create(
            prompt=user_input,
            size='256x256'  # 256x256, 512x512, and 1024x1024

        )
        print(response)
    return render(request, "main.html", {})


def main_home(request):
    return render(request, 'base.html')
