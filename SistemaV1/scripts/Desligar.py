GPIO_VENTOINHA = 5
GPIO_LED_MAIN = 6
GPIO_LEDS_SECUNDARIAS = [13, 19, 26]
GPIO_TRIGGER = 23
GPIO_ECHO = 24

def rodar_desligamento(ventoinha=None, sensor_hc=None, led_main=None, leds_secundarias=None):
    saidas = [ventoinha, led_main]

    if leds_secundarias is not None:
        saidas.extend(leds_secundarias)

    componentes = [*saidas, sensor_hc] # componentes = [["ventoinha", "led_main", "led_1"], "hc"]

    try:
        for saida in saidas:
            if saida is not None:
                saida.off()
    finally:
        for componente in componentes:
            if componente is not None:
                componente.close()

    raise SystemExit