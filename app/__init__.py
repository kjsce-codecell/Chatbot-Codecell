from flask import Flask

# Initialize the app
app = Flask(__name__, instance_relative_config=True,static_folder='static')

# Load the views
from app import views

# Load the config file
app.config.from_object('config')