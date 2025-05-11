import numpy as np
import yaml


class Distribuciones:
  def __init__(self, config=None):
      if config is not None:
         self.config = config
      else:
         with open("configuration.yaml", "r") as file:
              self.config = yaml.safe_load(file)
      
  def gaussiana(self, media, desviacion, N):
    media = self.config['distribuciones']['media_gaussiana']
    desvi = self.config['distribuciones']['gaussiana_desviacion']
    Num = self.config['simulacion']['N']
    dist = np.random.normal(media, desvi, Num)
    return dist
  
  def uniforme(self, valor_minimo, valor_maximo, N):
    min_val = valor_minimo if valor_minimo is not None else self.config['distribuciones']['uniforme_min']
    max_val = valor_maximo if valor_maximo is not None else self.config['distribuciones']['uniforme_max']
    Num = N if N is not None else self.config['simulacion']['N']
    dist = np.random.uniform(min_val, max_val, Num)
    return dist
