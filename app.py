from jinja2 import Environment, FileSystemLoader
from web import app
from aiogram import Bot, Dispatcher
from flask_sqlalchemy import SQLAlchemy

import configparser

cp = configparser.ConfigParser()
cp.read("config.ini")

app.config['SQLALCHEMY_DATABASE_URI'] = cp['server']['db']

db = SQLAlchemy(app)