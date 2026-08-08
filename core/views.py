from django.shortcuts import render
from dotenv import load_dotenv
import os
import markdown
import requests
load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key={API_KEY}"
def home(request):
    text_output=''
    if request.method == "POST":
        userinput = request.POST.get("question")
        payload = { 
            "contents" : [{
                "role":"user",
                "parts":[{"text":userinput}]
            }
            ],
        }
        response = requests.post(URL,json=payload).json()

        print(response)

        try:
            text_output = response["candidates"][0]["content"]["parts"][0]["text"]
            text_output = markdown.markdown(text_output)
        except KeyError:
            text_output = "error or unexpected response formate."

            
    return render(request,'coree/index.html',{"answer":text_output})