from car import Car
from car_factory import SimpleCarFactory


def buycar():
    car = None
    car = SimpleCarFactory.create_simple_car(car_type ="electric")
    car.cut_sheet_metal()
    car.press_metal()
    car.frame_welding()
    car.paint()
    car.part_assembly()
    car.drive_test()

    return car


if __name__ == "__main__" :
    buycar()


