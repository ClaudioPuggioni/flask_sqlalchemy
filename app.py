from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Middleware
cors = CORS(app)

from views import *
