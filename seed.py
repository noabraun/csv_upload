"""Utility file to seed bill database from the parsed data (parse.py)"""
import datetime
import os
from sqlalchemy import func
from server import app
from model import connect_to_db, db, Coordinate
# from test import read_csv
import csv

def read_csv():

    with open('example.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        count = 0

        for row in spamreader:
            if count == 0:
                count += 1
                pass
            else:
                print row #array
                #should loop through the row and push elements of the array into the DB
                location = row[0]
                date = row[1]
                notes = row[2]
                lattitude = row[3]
                lattitude_direction = row[4]
                longitude = row[5]
                print longitude
                longitude_direction = row[6]

                coordinate = Coordinate(location=location, date=date, notes=notes, lattitude=lattitude,
                                        lattitude_direction=lattitude_direction, longitude=longitude,
                                        longitude_direction=longitude_direction)

                db.session.add(coordinate)
                db.session.commit()
                count += 1


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    read_csv()


