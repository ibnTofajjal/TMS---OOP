from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, email, nid) -> None:
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount) -> None:
        super().__init__(name, email, nid)
        self.current_ride = None
        self.current_location = current_location
        self.wallet = initial_amount

    # Display Profile
    def display_profile(self):
        print(f"Rider Name: {self.name}, \n Email: {self.email}")

    # Load to Wallet
    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
        else:
            print("Amount is Less than 0")

    # Update Location
    def update_location(self, current_location):
        self.current_location = current_location

    # Request for a Ride
    def request_ride(self):
        pass

    # Show Current Ride
    def show_current_ride(self):
        print(self.current_ride)


class Driver(User):
    def __init__(self, name, email, nid, current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = 0

    # Display Profile
    def display_profile(self):
        print(f"Driver Name: {self.name}")

    # Accept The Ride
    def accept_ride(self, ride):
        pass