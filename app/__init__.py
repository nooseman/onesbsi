from flask import Flask
import sendgrid
import os
from sendgrid.helpers.mail import *
from validate_email import validate_email


app = Flask(__name__)
app.config.from_object('config')

sg = sendgrid.SendGridAPIClient(apikey=app.config['SENDGRID_API_KEY'])

from app import views

