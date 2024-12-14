from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Vehicle(ABC):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(f"{make} {model} (US Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(f"{make} {model} (US Spec)", model)


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(f"{make} {model} (EU Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(f"{make} {model} (EU Spec)", model)


def main():
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Ford", "Mustang")
    vehicle1.start_engine()
    vehicle2 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    vehicle2.start_engine()

    vehicle3 = eu_factory.create_car("Volkswagen", "Golf")
    vehicle3.start_engine()
    vehicle4 = eu_factory.create_motorcycle("Ducati", "Monster")
    vehicle4.start_engine()


if __name__ == "__main__":
    main()
