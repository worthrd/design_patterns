from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def cut_sheet_metal(self):
        pass
    
    @abstractmethod
    def press_metal(self):
    	pass


    @abstractmethod
    def frame_welding(self):
        pass

        
    @abstractmethod
    def paint(self):
        pass

    
    @abstractmethod
    def part_assembly(self):
        pass

    @abstractmethod
    def drive_test(self):
        pass
	

class ReliableCar(Car):

    def __init__(self):
        self.name = "Reliable Car"

    def cut_sheet_metal(self):
        print("ReliableCar cutting sheet metal")
    
    def press_metal(self):
        print("ReliableCar pressing metal")


    def frame_welding(self):
        print("ReliableCar frame welding!")

    def paint(self):
        print("ReliableCar paint")

    
    def part_assembly(self):
        print("ReliableCar part assembly")

    def drive_test(self):
        print("ReliableCar drive test")
	

class CheapCar(Car):

    def __init__(self):
        self.name = "Cheap Car"

    def cut_sheet_metal(self):
        print("CheapCar cutting sheet metal")
    
    def press_metal(self):
        print("CheapCar pressing metal")


    def frame_welding(self):
        print("CheapCar frame welding!")

    def paint(self):
        print("CheapCar paint")

    
    def part_assembly(self):
        print("CheapCar part assembly")

    def drive_test(self):
        print("CheapCar drive test")
	

class HighTechElectricCar(Car):

    def __init__(self):
        self.name = "High Tech Electric Car"

    def cut_sheet_metal(self):
        print("HighTechElectricCar cutting sheet metal")
    
    def press_metal(self):
        print("HighTechElectricCar pressing metal")


    def frame_welding(self):
        print("HighTechElectricCar frame welding!")

    def paint(self):
        print("HighTechElectricCar paint")

    
    def part_assembly(self):
        print("HighTechElectricCar part assembly")

    def drive_test(self):
        print("HighTechElectricCar drive test")

