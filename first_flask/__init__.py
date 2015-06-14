# run only once when package is imported, it creates all variables required to run the app
from flask import Flask
app = Flask(__name__)
app.config.from_object('config')
from first_flask import views, models




