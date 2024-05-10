
from datetime import datetime
class Rider():
    def __init__(self, start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None

    # Set a Driver For the Ride
    def set_driver(self, driver):
        self.driver = driver

    # Start Ride
    def start_ride(self):
        self.start_time = datetime.now()

    # End Ride
    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare 
        self.driver.wallet += self.estimated_fare 

    def __repr__(self) -> str:
        return f"Rider Details:----------------------------- \n Ride Started: {self.start_ride} \n Ride Ended: {self.end_ride}"