# main.py

from Checklist import rodar_checklist
from Rotina import rodar_rotina

def main():
    distancia_maxima = rodar_checklist() # distância máxima em centímetros.
    rodar_rotina(distancia_maxima)

if __name__ == "__main__":
    main()