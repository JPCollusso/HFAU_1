import requests

TOKEN = "SEU_TOKEN"
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

CHAT_IDS = [
    8821050002,
    1234567890,
]

def checklist_temperatura():

    def enviar_telegram(mensagem):
        for chat_id in CHAT_IDS:
            try:
                requests.post(
                    URL,
                    json={"chat_id": chat_id, "text": mensagem},
                    timeout=10
                )
            except requests.RequestException:
                pass

    def ler_temperatura_cpu() -> float | None:
        try:
            with open("/sys/class/thermal/thermal_zone0/temp", "r") as arquivo:
                return int(arquivo.read()) / 1000
        except OSError:
            return None
        
    temperatura = ler_temperatura_cpu()

    if temperatura is None:
        enviar_telegram("Não foi possível ler a temperatura da CPU")
        return None
    
    if temperatura >= 80.0:
        enviar_telegram(f"Temperatura da CPU altíssima: {temperatura:.1f}°C")
        return temperatura
    
    return temperatura

    
    