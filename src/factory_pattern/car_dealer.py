from car_factory import *
from car import *
from abc import ABC, abstractmethod


class CarDealer(ABC):

    """
    def __init__(self, factory: SimpleCiarFactory):
        self.factory = factory
    """


    def buy_a_car(self, car_type: str)-> Car:
        # car = self.factory.create_simple_car(car_type)
        # car = self.factory.create_simple_car(car_type)
        car = self.create_simple_car(car_type)
        car.cut_sheet_metal()
        car.press_metal()
        car.frame_welding()
        car.paint()
        car.part_assembly()
        car.drive_test()

        return car

    @abstactmethod
    def create_simple_car(car_type: str) -> Car
        pass

