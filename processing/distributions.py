import numpy as np

class Distribution():
  def _init_(self, N:int=None):
    self.N_ = N #aquí definimos que N sean los elementos que se generan
  #para el proyecto se nos pide una distribución normal y una uniforme
  def _normal_distribution(self, n:float = 0.0, f:float=0.0):
    val = np.random.normal(n, f, self._N)
    return val

  def _uniform_distribution(self, n:float = 0.0, f:float = 0.0):
    val = np.random.normal(n, f, self._N)
    return val
  
  #set nosdevuelve datos aleatorios, dependiendo de la distribución
  def set(self, init_val:float=None, fin_val:float=None, distribution:str=""):
        try:
            if distribution=="normal":
                var = self._normal_distribution(init_val, fin_val)
            elif distribution=="uniform":
                var = self._uniform_distribution(init_val, fin_val)
            else:
                raise Exception("No hay distribucion")
            return var
        except Exception as e:
            print(f"Error: {e}")

    
