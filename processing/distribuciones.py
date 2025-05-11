import random

def generar_masa_gaussiana(media=10, desviacion=2):
    """Genera una masa con distribución normal."""
    return max(1, random.gauss(media, desviacion))  # evitar masas negativas o cero

def generar_posicion_uniforme(ancho, alto, margen=100):
    """Genera una posición aleatoria uniforme dentro de los límites del espacio."""
    x = random.uniform(margen, ancho - margen)
    y = random.uniform(margen, alto - margen)
    return x, y
