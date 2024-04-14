from flask import Flask, render_template, request, redirect, url_for,flash,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker, scoped_session
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///election4.db'
db = SQLAlchemy(app)
