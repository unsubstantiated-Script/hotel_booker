import pandas

df = pandas.read_csv('hotels.csv')


class Hotel:
    def __init__(self, id):
        pass

    def available(self):
        pass

    def book(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass

    @staticmethod
    def generate():
        content = f"Name of the customer hotel"
        return content


print(df)

id = input("Enter hotel id: ")

hotel = Hotel(id)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("No hotel available")
