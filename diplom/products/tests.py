from django.test import TestCase

# Create your tests here.


import os
import openai

openai.api_key = "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"

messages = [{"role" : "user", "content" : "напиши слово привет"}]

response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                        messages=messages,
                                        temperature=0.5,
                                        max_tokens=1000)