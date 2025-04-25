class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start_engine(self):
        print(f"{self.engine_type} engine started.")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Composition: Engine object is passed to Car class

    def start_car(self):
        print(f"Starting the {self.brand} car...")
        self.engine.start_engine()  # Access Engine's method through Car

# Create an Engine object
engine1 = Engine("V8")

# Create a Car object and pass the Engine object to it
car1 = Car("Tesla", engine1)

# Start the car, which will start the engine as well
car1.start_car()
