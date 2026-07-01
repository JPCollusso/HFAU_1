import time
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt

TRIG = 23 # Mutável
ECHO = 24 # Mutável

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, GPIO.LOW)
time.sleep(0.2)

def distancia_cm():
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)   # pulso de 10 us
    GPIO.output(TRIG, GPIO.LOW)

    t0 = time.time()
    while GPIO.input(ECHO) == GPIO.LOW:
        if time.time() - t0 > 0.03:
            return None

    inicio = time.time()
    while GPIO.input(ECHO) == GPIO.HIGH:
        if time.time() - inicio > 0.03:
            return None

    return (time.time() - inicio) * 17150

plt.ion()
fig, ax = plt.subplots()

linha_1s, = ax.plot([], [], "o-", label="Leitura a cada 1 s")
linha_02s, = ax.plot([], [], ".-", label="Leitura a cada 0.2 s")

t_1s, d_1s = [], []
t_02s, d_02s = [], []

inicio = time.time()
proxima_1s = 0

ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Distância (cm)")
ax.legend()

try:
    while plt.fignum_exists(fig.number):
        agora = time.time() - inicio
        d = distancia_cm()

        if d is not None:
            t_02s.append(agora)
            d_02s.append(d)

            if agora >= proxima_1s:
                t_1s.append(agora)
                d_1s.append(d)
                proxima_1s += 1

        linha_02s.set_data(t_02s, d_02s)
        linha_1s.set_data(t_1s, d_1s)

        ax.relim()
        ax.autoscale_view()
        plt.pause(0.2)

finally:
    GPIO.output(TRIG, GPIO.LOW)
    GPIO.cleanup()