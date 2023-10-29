#!/usr/bin/python3
"""
    Creating an api
"""
import models
from os import getenv
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blue_print(app_views)


@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST') if getenv('HBNB_API_HOST') else '0.0.0.0'
    port = getenv('HBNB_API_PORT') if getenv('HBNB_API_PORT') else '5000'
    app.run(host=host, port=port, threaded=True)
