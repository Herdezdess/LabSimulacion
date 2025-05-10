import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
from processing.distribuciones import Distribuciones

class Objeto:
  def __init__(self, tipo, config):
    self.tipo = tipo
    self.masa = max(1, gauss(config["media_masa"], config["desviacion_masa"]))
    self.y = unif(0, config['ancho'])
    self.x = unif(0, config['alto'])
    self.velocidad_x = 0
    self.velocidad_y = 0
    self.radio = int(self.masa ** (1/2))
    self.color = color

  def crear_figura(self, pantalla):
    tamaño = self.masa * M #M es la proporcion entre la masa y el tamaño del objeto

    if self.tipo == "circulo":
      pygame.draw.circle(pantalla, self.color, (int(self.x), int(self.y)), self.radio)
    elif self.tipo == "cuadrado":
      pygame.draw.rect(pantalla, sel.color, (self.x - tamaño, self.y - tamaño), 2 * tamaño, 2 * tamaño)
    elif self.tipo == "triangulo":
      puntos = [
          (self.x, self.y + tamaño),
          (self.x - tamaño, self.y - tamaño),
          (self.x + tamaño, self.y - tamaño)
      ]
      pygame.draw.polygon(pantalla, self.color, puntos)

class Generador:
  def __init__(self, config):
    self.config = config

  def generar_objetos(self):
    objetos = []
    num_objetos = self.config['simulacion']['N']
    gauss_media = self.config['distribuciones']['gaussiana_media']
    gauss_desviacion = self.config['distribuciones']['gaussiana_desviacion']
    uniforme_min = self.config['distribuciones']['uniforme_min']
    uniforme_max = self.config['distribuciones']['uniforme_max']

    for _ in range(num_objetos):
      tipo = random.choice(["circulo", "cuadrado", "triangulo"])
      masa = Distribuciones.gaussiana(gauss_media, gauss_desviacion)
      x, y = Distribuciones.uniforme(uniforme_min, uniforme_max)
      color = np.random.rand(3) #el random.rand genera numeros float aleatorios en el intervalo [0, 1).
    #El resultado de esta ultima parte, deberia tener la forma array([0.653, 0.234, 0.987]). Eso nos va a dar un color RGB aleatorio
      objetos.append(Objeto(tipo, masa, x, y, color))
    return objetos
