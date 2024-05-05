import pandas

df = pandas.read_csv('hotels.csv', dtype={"id": str})


class Hotel:
    watermark = "Joe's crabs and stuffz"

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()

    def book(self):
        """Book a hotel by changing its availability to not-available."""
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        """" Check if hotel is available """
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()

        if availability == 'yes':
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation.
        Here is your booking information:
        Name: {self.customer_name}
        Hotel Name: {self.hotel.name}
        """
        return content
