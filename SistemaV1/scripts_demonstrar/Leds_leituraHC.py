import time
import RPi.GPIO as GPIO

TRIG = 23 # Mutável
ECHO = 24 # Mutável

LED_VERMELHO = 17 # Mutável
LED_AMARELO = 27  # Mutável
LED_VERDE = 22    # Mutável

GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

for led in [LED_VERMELHO, LED_AMARELO, LED_VERDE]:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.LOW)

GPIO.output(TRIG, GPIO.LOW)
time.sleep(0.2)

dist_vermelho = float(input("Acender LED vermelho até quantos cm? "))
dist_amarelo = float(input("Acender LED amarelo até quantos cm? "))
dist_verde = float(input("Acender LED verde até quantos cm? "))

def medir_distancia():
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)

    inicio_timeout = time.time()
    while GPIO.input(ECHO) == GPIO.LOW:
        if time.time() - inicio_timeout > 0.03:
            return None

    inicio = time.time()

    while GPIO.input(ECHO) == GPIO.HIGH:
        if time.time() - inicio > 0.03:
            return None

    tempo = time.time() - inicio
    return tempo * 17150

def apagar_leds():
    GPIO.output(LED_VERMELHO, GPIO.LOW)
    GPIO.output(LED_AMARELO, GPIO.LOW)
    GPIO.output(LED_VERDE, GPIO.LOW)

try:
    while True:
        distancia = medir_distancia()

        if distancia is not None:
            print(f"Distância: {distancia:.1f} cm")

            apagar_leds()

            if distancia <= dist_vermelho:
                GPIO.output(LED_VERMELHO, GPIO.HIGH)
            elif distancia <= dist_amarelo:
                GPIO.output(LED_AMARELO, GPIO.HIGH)
            elif distancia <= dist_verde:
                GPIO.output(LED_VERDE, GPIO.HIGH)

        time.sleep(0.2)

except KeyboardInterrupt:
    print("Encerrando...")

finally:
    apagar_leds()
    GPIO.output(TRIG, GPIO.LOW)
    GPIO.cleanup()