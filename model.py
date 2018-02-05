from flask_sqlalchemy import SQLAlchemy
from collections import defaultdict

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///bills'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


class Coordinate(db.Model):
    """Coordinate metadata"""

    __tablename__ = "coordinates"

    coordinate_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    location = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime)
    notes = db.Column(db.Text, nullable=True)
    lattitude = db.Column(db.Float, nullable=False)
    lattitude_direction = db.Column(db.String(8))
    longitude = db.Column(db.Float, nullable=True)
    longitude_direction = db.Column(db.String(8))


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Coordinate coordinate_id=%s location=%s date=%s notes=%s lattitude=%s lattitude_direction=%s longitude=%s longitude_direction=%s >" % (self.coordinate_id, self.location, self.date, 
                                                                                   self.notes, self.lattitude, self.lattitude_direction, self.longitude, self.longitude_direction)



def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///coordinates'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app

    connect_to_db(app)
    print "Connected to DB."