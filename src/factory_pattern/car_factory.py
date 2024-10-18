from car import *

class SimpleCarFactory:
    def create_simple_car(car_type: str) -> Car:
        if car_type == "electric":
            return HighTechElectricCar()
