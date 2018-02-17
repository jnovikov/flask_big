from flask import jsonify
from time import time


def index_api():
    return jsonify({'hello': 'World'})


def time_api():
    return jsonify({"time": time()})
