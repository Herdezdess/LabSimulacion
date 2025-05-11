import numpy as np
import random


class Distribuciones:
  def __init__(self, config=None):
      if config is not None:
         self.config = config
      else:
         with open("configuration.yaml", "r") as file:
              self.config = yaml.safe_load(file)
      
  def gaussiana(self, media, desviacion, N):
    return np.random.normal(media,desviacion,N)
  
  def uniforme(self, valor_minimo, valor_maximo, N):
    return [random.uniform(valor_minimo, valor_maximo) for _ in range(N)]
