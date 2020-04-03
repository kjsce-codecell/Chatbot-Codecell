from app import views
from flask import Flask

# Initialize the app
app = Flask(__name__, instance_relative_config=True, static_folder='static')

# Load the views

# Load the config file
app.config.from_object('config')
