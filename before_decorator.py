class CarCWashBase():

  def __init__(self,hasPolishing = False, hasCarpetClean=False, hasSeatClean = False):
    self.hasPolishing = hasPolishing
    self.hasCarpetClean = hasCarpetClean
    self.hasSeatClean = hasSeatClean
    self.price = 0.0

  def cost(self):
    if self.hasPolishing:
      self.price+= 70.0
    
    if self.hasCarpetClean:
      self.price+= 60.0
    
    if self.hasSeatClean:
      self.price+= 90.0
    
    return self.price
    



class HatchbackWash(CarCWashBase):
  def __init__(self,hasPolishing = False, hasCarpetClean=False, hasSeatClean = False):
    super().__init__(hasPolishing,hasCarpetClean,hasSeatClean)
    self.price = 100

class SedanWash(CarCWashBase):
  def __init__(self,hasPolishing = False, hasCarpetClean=False, hasSeatClean = False):
    super().__init__(hasPolishing,hasCarpetClean,hasSeatClean)
    self.price = 120


class TruckWash(CarCWashBase):
  def __init__(self,hasPolishing = False, hasCarpetClean=False, hasSeatClean = False):
    super().__init__(hasPolishing,hasCarpetClean,hasSeatClean)
    self.price = 200


car1Wash = HatchbackWash(False, True, True)

print(car1Wash.cost())

