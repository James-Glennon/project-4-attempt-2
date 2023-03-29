from bookingmanager import db


class AllBookings(db.Model):
    # Schema for all bookings model
    id = db.Column(db.Integer, primary_key="True")
    name = db.Column(db.String, nullable="False")
    email = db.Column(db.String, nullable="False")
    phone = db.Column(db.Integer, nullable="False")
    booking_date = db.Column(db.Date, nullable="False")
    booking_time = db.Column(db.Time, nullable="False")
    daybookings = db.relationship(
        "DayBookings", backref="allbookings", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.name


class DayBookings(db.Model):
    # schema model for booking for a single date
    id = db.Column(db.Integer, primary_key="True")
    booking_date = db.Column(db.Date, db.ForeignKey(
        "allbookings.booking_date"), nullable="False")
    booking_time = db.Column(db.Time, nullable="False")
    name = db.Column(db.String, nullable="False")

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"#{self.id}"
