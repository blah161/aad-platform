from flask import Blueprint, redirect

aegon = Blueprint("aegon", __name__)

@aegon.route("/")
def home():
    return redirect("https://aegon-core.onrender.com")
