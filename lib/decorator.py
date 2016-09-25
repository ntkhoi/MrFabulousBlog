__author__ = 'bluzky'
from functools import wraps
from flask import session, redirect, current_app, url_for, request

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "logged_in" not in session:
            return redirect(url_for("login", next=request.url))
        else:
            return func(*args, **kwargs)
    return wrapper
