from flask import render_template, Blueprint


storefront = Blueprint("store", __name__, url_prefix="/store")

@storefront.route('/', methods=['GET'], strict_slashes=False)
def index():
    return render_template('store.html')