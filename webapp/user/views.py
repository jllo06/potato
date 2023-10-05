from flask import Blueprint, render_template, session, redirect
from functools import wraps

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')