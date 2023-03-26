from flask import Blueprint, render_template


menu = Blueprint("menu",__name__)


@menu.route("/")
def login_init():
    return render_template('views/login.html')


@menu.route("/homepage")
def index():
    return render_template('index.html')


@menu.route("/prospectar")
def prospectar():
    return render_template('views/prospectar.html')