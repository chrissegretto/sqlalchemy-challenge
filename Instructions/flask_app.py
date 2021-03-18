import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# View all of the classes that automap found
Base.classes.keys()

# Save references to each table
measurement = Base.classes.measurement
stations = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    # session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    precip_scores = session.query(measurement.date,measurement.prcp).all()

    # session.close()
    percip=[]
    for precip in precip_scores:
        scores = {}
        scores["date"]=precip[0]
        scores["prcp"]=precip[1]
        percip.append(scores)

    # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    return jsonify(percip)


@app.route("/api/v1.0/stations")
def station_v():
#   * Return a JSON list of stations from the dataset.


    """Return a list of all passenger names"""
    # Query all passengers
    station_results = session.query(stations.station).all()

    # session.close()
    station_list=[]
    for st in station_results:
        scores = {}
        scores["station name"]=st[0]
        # scores["prcp"]=precip[1]
        station_list.append(scores)

    # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    return jsonify(station_list)


# @app.route("/api/v1.0/passengers")
# def passengers():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of passenger data including the name, age, and sex of each passenger"""
#     # Query all passengers
#     results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

#     session.close()

#     # Create a dictionary from the row data and append to a list of all_passengers
#     all_passengers = []
#     for name, age, sex in results:
#         passenger_dict = {}
#         passenger_dict["name"] = name
#         passenger_dict["age"] = age
#         passenger_dict["sex"] = sex
#         all_passengers.append(passenger_dict)

#     return jsonify(all_passengers)


if __name__ == '__main__':
    app.run(debug=True)
