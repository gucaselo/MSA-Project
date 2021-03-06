# import necessary libraries
from flask import Flask, render_template, jsonify
import sqlalchemy
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# create instance of Flask app
app = Flask(__name__)

# create route that renders index.html template
@app.route("/")

def index():
    return render_template('index.html')

# create route that returns mass shooting incidents
@app.route("/msa")
def msa():

    # Create Engine
    engine = create_engine("sqlite:///Data/shootings.sqlite")

    # Connect to the engine
    conn = engine.connect()

    # Start a session
    session = Session(bind=engine)

    # Declare a Base using `automap_base()`
    Base = automap_base()

    # Use the Base class to reflect the database tables
    Base.prepare(engine, reflect=True)

    # Assign class to variable data
    data = Base.classes.shooting_data

    # Create variables for the shooting incident dictionary
    lng = session.query(data.longitude).all()
    lat = session.query(data.latitude).all()
    killed = session.query(data.number_killed).all()
    injured = session.query(data.number_injured).all()
    date = session.query(data.incident_date).all()
    state = session.query(data.state).all()
    locale = session.query(data.city_county).all()

    incidents = []
    # Create shooting data dictionary to be returned
    for i in range(len(date)):
        incident_list = {'date': date[i],
                        'state': state[i],
                        'city_county': locale[i],
                        'longitude': lng[i],
                        'latitude': lat[i],
                        'killed': killed[i],
                        'injured': injured[i]}

        incidents.append(incident_list)

    # Close session
    session.close()

    return jsonify(incidents)

# create route that returns gun ownership data
@app.route("/guns")
def guns():

    # Create Engine
    engine = create_engine("sqlite:///data/shootings.sqlite")

    # Connect to the engine
    conn = engine.connect()

    # Start a session
    session = Session(bind=engine)

    # Declare a Base using `automap_base()`
    Base = automap_base()

    # Use the Base class to reflect the database tables
    Base.prepare(engine, reflect=True)

    # Assign class to variable data
    guns = Base.classes.ownership_data

    # Create variables for the gun ownership dictionary
    gun_states = session.query(guns.state).all()
    gun_capita = session.query(guns.number_per_capita).all()
  
    ownership = []

    # Create gun ownership dictionary to be returned
    for i in range(len(gun_states)):
        gun_list = {'state': gun_states[i],
                'num_guns': gun_capita[i]}

        ownership.append(gun_list)

    # Close session
    session.close()

    return jsonify(ownership)

# create route that returns poverty data
@app.route("/poverty")
def poverty():

    # Create Engine
    engine = create_engine("sqlite:///data/shootings.sqlite")

    # Connect to the engine
    conn = engine.connect()

    # Start a session
    session = Session(bind=engine)

    # Declare a Base using `automap_base()`
    Base = automap_base()

    # Use the Base class to reflect the database tables
    Base.prepare(engine, reflect=True)

    # Assign class to variable data
    poverty = Base.classes.poverty_data

    # Create variables for the poverty rate dictionary
    poverty_states = session.query(poverty.state).all()
    poverty_rates = session.query(poverty.poverty_rate).all()
  
    poverty_data = []

    # Create poverty rate dictionary to be returned
    for i in range(len(poverty_rates)):
    
        poverty_list = {'state' : poverty_states[i],
                'poverty_rates': poverty_rates[i]}

        poverty_data.append(poverty_list)
            

    # Close session
    session.close()

    return jsonify(poverty_data)

    # create route that returns election data
@app.route("/election")
def election():

    # Create Engine
    engine = create_engine("sqlite:///data/shootings.sqlite")

    # Connect to the engine
    conn = engine.connect()

    # Start a session
    session = Session(bind=engine)

    # Declare a Base using `automap_base()`
    Base = automap_base()

    # Use the Base class to reflect the database tables
    Base.prepare(engine, reflect=True)

    # Assign class to variable data
    election = Base.classes.election_data

    # Create variables for the election info
    state_name = session.query(election.state).all()
    state_result = session.query(election.result).all()
  
    election_data = []

    # Create election dictionary to be returned
    for i in range(len(state_name)):
    
        election_list = {'state' : state_name[i],
                'result': state_result[i]}

        election_data.append(election_list)
            

    # Close session
    session.close()

    return jsonify(election_data)

    
    # create route that returns state data
@app.route("/state")
def state():

    # Create Engine
    engine = create_engine("sqlite:///data/shootings.sqlite")

    # Connect to the engine
    conn = engine.connect()

    # Start a session
    session = Session(bind=engine)

    # Declare a Base using `automap_base()`
    Base = automap_base()

    # Use the Base class to reflect the database tables
    Base.prepare(engine, reflect=True)

    # Assign class to variable data
    state = Base.classes.state_data

    # Create variables for the election info
    state_name = session.query(state.state).all()
    state_lat = session.query(state.latitude).all()
    state_long = session.query(state.longitude).all()
  
    state_data = []

    # Create election dictionary to be returned
    for i in range(len(state_name)):
    
        state_list = {'state' : state_name[i],
                'latitude': state_lat[i],
                'longitude': state_long[i]}

        state_data.append(state_list)
            

    # Close session
    session.close()

    return jsonify(state_data)

if __name__ == "__main__":
    app.run(debug=True)