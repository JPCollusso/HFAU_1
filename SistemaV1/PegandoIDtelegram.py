import requests

TOKEN = "8710912164:AAF8Jsar57Y2fg1nGW8fBS0kqJdgqneYdCI"
CHAT_ID = 8821050002

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"


i = "haha"
requests.post(url, json={"chat_id": CHAT_ID, "text": f"carro {i}"})
print(f"Mensagem {i} enviada")