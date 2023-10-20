import os
from app import app
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


load_dotenv()

url = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = url
db = SQLAlchemy(app)


with app.app_context():
    db.create_all()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
