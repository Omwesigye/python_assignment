class Booking:
    def confirm_booking(self):
        print("Confirming general booking")

class FlightBooking(Booking):
    def confirm_booking(self):
        print("Confirming flight booking with airlines ")

class TrainBooking(Booking):
    def confirm_booking(self):
        print("Confirming train booking with railway ")

flight_booking = FlightBooking()
flight_booking.confirm_booking() 
