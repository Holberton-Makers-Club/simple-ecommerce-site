from flask import render_template, Blueprint
import requests
from helpers import build_url


storefront = Blueprint("store", __name__, url_prefix="/store")

@storefront.route('/', methods=['GET'], strict_slashes=False)
def index():
    data = {}
    r = requests.get(build_url('api/products')).json()
    if not r.get('status') == 'OK':
        data['msg'] = 'API error'
    data['products'] = r.get('products')
    return render_template('store.html', data=data)