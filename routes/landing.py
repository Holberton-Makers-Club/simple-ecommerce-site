from flask import render_template, Blueprint


landing = Blueprint("landing", __name__, url_prefix="/")

@landing.route('/', methods=['GET'], strict_slashes=False)
def index():
    return render_template('landing.html')