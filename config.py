import os
from dotenv import load_dotenv

load_dotenv()
BALLEDONTLIE_API_KEY = os.getenv("BALLEDONTLIE_API_KEY")


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'ynov.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'change-this-to-a-random-secret'
