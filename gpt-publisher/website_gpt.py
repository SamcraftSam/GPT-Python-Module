import os
import openai
openai.api_key = "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"

prompt_setup = "Привіт, ти редактор сайту новин. У кожному наступному повідомленні я надаватиму тобі певну новину у вигляді статті. Ти маєш творчо підійти до завдання, і перефразувати цю новину, зберігши зміст. Просто перефразуй її. Відповідай тільки результатом, без передмов. Новина має відповідати на питання 'Що? Де? Як? Коли? Чому?' Розмір статті до 1000 символів"
with open("test.txt", "r") as f:
    prompt_new = f.read() #test purposes

def query(prompt):
    responce  = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        max_tokens=1200,
        temperature=0.4
        )
    return responce["choices"][0]["text"]

query(prompt_setup)
print(query(prompt_new))