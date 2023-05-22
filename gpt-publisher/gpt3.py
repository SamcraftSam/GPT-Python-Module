import os
import openai

openai.api_key = "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"

def chat(messags, message):
    #global messages
    messags.append({"role": "assistant", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messags
    )
    messags.append({"role": "assistant", "content": response["choices"][0]["message"].content})
    return response["choices"][0]["message"]["content"]

