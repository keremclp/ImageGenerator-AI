from django.shortcuts import render
import openai
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('OPENAI_KEY', None)
openai.api_key = api_key


def main_home(request):
    return render(request, 'base.html')
