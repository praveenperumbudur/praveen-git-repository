class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity
    
    def fare(self):
        total_fare = self.seating_capacity * 100
        if isinstance(self, Bus):
            total_fare += total_fare * 0.1  # Add 10% maintenance charge for Bus
        return total_fare
# Example usage:
if __name__ == "__main__":
    bus1 = Bus(120, 12, 50)
    print(f"Max Speed: {bus1.max_speed} km/h")
    print(f"Mileage: {bus1.mileage} km/l")
    print(f"Seating Capacity: {bus1.seating_capacity}")
    print(f"Total Fare: ${bus1.fare()}")
    bus2 = Bus(100, 10, 30)
    print(f"Max Speed: {bus2.max_speed} km/h")
    print(f"Mileage: {bus2.mileage} km/l")
    print(f"Seating Capacity: {bus2.seating_capacity}")
    print(f"Total Fare: ${bus2.fare()}")
