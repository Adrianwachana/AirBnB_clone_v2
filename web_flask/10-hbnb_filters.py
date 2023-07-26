#!/usr/bin/python3
# list of states
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity  # Import your Amenity model class here

app = Flask(__name__)


@app.teardown_appcontext
def close_db(exception):
    """Close the current SQLAlchemy session after each request."""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def state_list():
    """Display a HTML page with filters for states, cities, and amenities."""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda a: a.name)  # Replace Amenity with your Amenity model class

    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

