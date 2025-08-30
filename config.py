import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'ynov.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'change-this-to-a-random-secret'
BALLEDONTLIE_API_KEY = "9dde42a4-9826-40ea-8b1d-8f27373f7110"
