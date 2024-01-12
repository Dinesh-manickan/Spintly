from flask import Flask

app = Flask(__name__)

# All the apis in single file
from app.api import apis

# Error handling
from app import error

