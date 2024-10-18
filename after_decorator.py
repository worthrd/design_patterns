class CarWashBase():
  def __init__(self):
    self.price = 0.0

  def cost(self):
    return self.price

class DecoratorBase(CarWashBase):
   def __init__(self, car_wash):
    self.car_wash =  car_wash

   def cost(self):
      return self.price + self.car_wash.cost()

class Polish(DecoratorBase):
   def __init__(self, car_wash):
    super().__init__(car_wash)
    self.price = 70

class CarpetClean(DecoratorBase):
   def __init__(self, car_wash):
    super().__init__(car_wash)
    self.price = 60

class SeatClean(DecoratorBase):
   def __init__(self, car_wash):
    super().__init__(car_wash)
    self.price = 90



class HatchbackWash(CarCWashBase):
  def __init__(self):
    self.price = 100

class SedanWash(CarCWashBase):
  def __init__(self):
    self.price = 120


class TruckWash(CarCWashBase):
  def __init__(self):
    self.price = 200


car1Wash = SeatClean(CarpetClean(HatchbackWash()))

car1Wash.cost()