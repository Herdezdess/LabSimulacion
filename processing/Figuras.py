import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np 
import random 
from distribuciones import distribucion_gaussiana as gauss
from distribuciones import distribucion_uniforme as unif

class Objeto:
  Formas = ["circulo", "cuadrado", "triangulo"]
   #Formas es una lista donde se va a guardar el nombre para cada una de las figuras
  def __init__(self, x, y, masa):
    self.x = x
    self.y = y
    self.masa = masa
    self.forma = random.choice(self.Formas)
    self.color = np.random.rand(3) #el random.rand genera numeros float aleatorios en el intervalo [0, 1). 
    #El resultado de esta ultima parte, deberia tener la forma array([0.653, 0.234, 0.987]). Eso nos va a dar un color RGB aleatorio

  def crear_figura(self, ax):
    tamaño = self.masa * M #M es la proporcion entre la masa y el tamaño del objeto 

    if self.forma == "circulo":
      figura = patches.Circle((self.x, self.y), radius=tamaño, color=self.color)
      #El primer parametro nos da el centro de la figura que vamos a crear
      #El segundo parametro nos indica el radio que va a tener la figura 
      #El tercer parametro nos da el color de la figura 
    elif self.forma == "cuadrado":
      figura = patches.Rectangle((self.x - tamaño, self.y - tamaño), 2 * tamaño, 2 * tamaño, color=self.color)
      #El primer parametro es la esquina inferior izquierda del cuadrado. Al resta el tamño, centra el cuadrado en (self.x, self.y)
      #El segundo parametro es el ancho del cuadrado (2*tamaño)
      #El tercer parámetro es el alto del rectangulo (2*tamaño)
      #El cuatro parametro es el color de la figura
    elif self.forma == "triangulo":
      puntos = [
          (self.x, self.y + tamaño),
          (self.x - tamaño, self.y - tamaño),
          (self.x + tamaño, self.y - tamaño)
      ]
      figura = patches.Polygon(puntos, closed=True, color=self.color)
      #En la parte de puntos, primero se define el vertice superior y luego los dos vertices de abajo que están a la misma altura. 
      #El primer parametro son los vertices del poligono 
      #Closed es solo para asegurarnos que la figura esté cerrada
      #El ultimo parametro es el color de la figura 
    ax.add_patch(figura)
    #Con esto dibujamos las diferentes figuras 

class sistema:
  def __init__(self, N):
    self.objetos = []
    masas = gauss(MED, DESV, N)
    posiciones_en_x = unif(0, L, N)
    posiciones_en_y = unif(0, L, N)

    for x, y, m in zip(posiciones_en_x, posiciones_en_y, masas):
      self.objetos.append(Objeto(x, y, m))
