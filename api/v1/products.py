from api.v1 import api_v1
from models.product import Product
from flask import jsonify


@api_v1.route('/products', methods=['GET'], strict_slashes=False)
def get_all_products():
    all_products = Product.get_by_class()
    if not all_products:
        return jsonify({
            'status': 'error',
            'message': 'database failure'
        }), 400
    return jsonify({
        'status': 'OK',
        'message': 'products retrieved',
        'products': all_products
    }), 200