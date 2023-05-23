from gpt3 import *

prompt_setup = "У кожному наступному повідомленні я надаватиму тобі певну новину у вигляді статті. Ти маєш творчо підійти до завдання, і перефразувати цю новину, зберігши зміст. Просто перефразуй її. Відповідай тільки результатом, без передмов. Новина має відповідати на питання 'Що? Де? Як? Коли? Чому?' Розмір статті до 1000 символів"
with open("test.txt", "r") as f:
    prompt_new = f.read() #test purposes

messags = [
    {"role": "assistant", "content": prompt_setup},
]
print("Its test script for gpt3 generator library!")
print(header(prompt_new))
print("#########################################################################################")
print(publication(prompt_new))
print("=========================================================================================")
print(message(prompt_new))
