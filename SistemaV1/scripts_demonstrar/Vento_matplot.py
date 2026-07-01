import time
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt

FAN_PIN = 18          # GPIO BCM
PWM_FREQ = 1000       # Hz
VEL_INTERMEDIARIA = 50  # %

def temperatura_cpu():
    with open("/sys/class/thermal/thermal_zone0/temp") as f:
        return int(f.read()) / 1000

def escolher_opcao():
    print("1 - Ventoinha ligada no máximo + gráfico")
    print("2 - Ventoinha em velocidade intermediária + gráfico")
    while True:
        op = input("Escolha 1 ou 2: ")
        if op in ("1", "2"):
            return op

GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT)

pwm = GPIO.PWM(FAN_PIN, PWM_FREQ)
pwm.start(0)

opcao = escolher_opcao()
velocidade = 100 if opcao == "1" else VEL_INTERMEDIARIA
pwm.ChangeDutyCycle(velocidade)

plt.ion()
fig, ax = plt.subplots()
linha, = ax.plot([], [], "r-")

tempos = []
temperaturas = []
inicio = time.time()

ax.set_title(f"Temperatura interna do Raspberry Pi - ventoinha {velocidade}%")
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Temperatura (°C)")

try:
    while plt.fignum_exists(fig.number):
        t = time.time() - inicio
        temp = temperatura_cpu()

        tempos.append(t)
        temperaturas.append(temp)

        linha.set_data(tempos, temperaturas)
        ax.relim()
        ax.autoscale_view()

        print(f"Temperatura: {temp:.1f} °C | Ventoinha: {velocidade}%")
        plt.pause(1)

except KeyboardInterrupt:
    print("Encerrando...")

finally:
    pwm.ChangeDutyCycle(0)
    pwm.stop()
    GPIO.output(FAN_PIN, GPIO.LOW)
    GPIO.cleanup()