from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)

# Middleware
# cross_origin(["http://www.domain1.com", "http://www.domain2.com"])
cors = CORS(app)

from views import *
