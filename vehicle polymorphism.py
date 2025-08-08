class BMW:
    def start_engine(self):
        print("BMW engine started with a smooth purr.")
    def stop_engine(self):
        print("BMW engine stopped.")
    def drive(self):
        print("Driving BMW... Luxurious and comfortable ride!")
class FERRARI:
    def start_engine(self):
        print("FERRARI engine roars to life with excitement!")
    def stop_engine(self):
        print("FERRARI engine shut down.")
    def drive(self):
        print("Driving FERRARI... Fast and thrilling experience!")
def test_drive(car):
    car.start_engine()
    car.drive()
    car.stop_engine()
    print("-" * 40)
bmw_car = BMW()
ferrari_car = FERRARI()
for vehicle in (bmw_car, ferrari_car):
    test_drive(vehicle)
