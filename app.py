import numpy as np
import datetime as dt 
from datetime import datetime

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, json

#Create the engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

measurement = Base.classes.measurement
station = Base.classes.station

app = Flask(__name__)


@app.route("/")
def Home_page():
    return(
        f"Available Routes: <br/>"
        f"api/v1.0/precipitation"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/august<br/>"
        f"/api/v1.0/august/21st<end>"
        

    )
@app.route("api/v1.0/precipitation")
def Precipitation():
        session = Session(engine)


        return jsonify(precip_results)
    
@app.route("/api/v1.0/stations")
def Stations():
        session = Session(engine)
        stations = session.query(measurement).group_by(measurement.station).count()

        return jsonify(precip_results)
    
@app.route("/api/v1.0/tobs")
def Temperture():
        session = Session(engine)
        
        return jsonify(precip_results)  
    
@app.route("/api/v1.0/august")
def Temperture():
        session = Session(engine)
        return jsonify(precip_results)

@app.route("/api/v1.0/august/21st")
def Temperture():
        session = Session(engine)
        stardate = '2017-08-01'
        cleanstardate = datetaime.strptime(startdate, '%Y-%m-%d')
        after_time = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.ave(measurement.tobs)).\
                filter(measurement.date>startdate).all()
        return jsonify(precip_results)


if __name__ == "__main__":
    app.run(debug=True)









