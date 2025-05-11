import pygame
import random
import numpy as np
from multiprocessing import Process
import time

ANCHO = 800
ALTO = 600
N_OBJETOS = 20

class Pelota:
    def __init__(self):
        self.x = random.randint(0, ANCHO)
        self.y = random.randint(0, ALTO)
        self.masa = abs(np.random.normal(loc=10, scale=5))
        self.color = tuple((np.random.rand(3) * 255).astype(int))
        self.forma = random.choice(["circulo", "cuadrado", "triangulo"])
        self.radio = int(self.masa) + 5
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)

    def mover(self):
        self.x += self.vx
        self.y += self.vy

        # Rebote en los bordes
        if self.x < 0 or self.x > ANCHO:
            self.vx *= -1
        if self.y < 0 or self.y > ALTO:
            self.vy *= -1

    def dibujar(self, pantalla):
        if self.forma == "circulo":
            pygame.draw.circle(pantalla, self.color, (int(self.x), int(self.y)), self.radio)
        elif self.forma == "cuadrado":
            pygame.draw.rect(pantalla, self.color,
                             (int(self.x - self.radio), int(self.y - self.radio),
                              2 * self.radio, 2 * self.radio))
        elif self.forma == "triangulo":
            puntos = [
                (int(self.x), int(self.y - self.radio)),
                (int(self.x - self.radio), int(self.y + self.radio)),
                (int(self.x + self.radio), int(self.y + self.radio))
            ]
            pygame.draw.polygon(pantalla, self.color, puntos)

def run_simulation():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Simulación de Objetos Aleatorios")

    objetos = [Pelota() for _ in range(N_OBJETOS)]
    reloj = pygame.time.Clock()
    corriendo = True

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        pantalla.fill((0, 0, 0))

        for obj in objetos:
            obj.mover()
            obj.dibujar(pantalla)

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()

if __name__ == "__main__":
    p = Process(target=run_simulation)
    p.start()
    p.join()

