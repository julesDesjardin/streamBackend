from functools import wraps

from flask import Flask, jsonify, request


def get_payload(func):
    """Decorator that extracts GET query params and wraps response."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        payload = request.args.to_dict()
        result = func(payload)
        print(f"Returned: {result}")
        return jsonify(success=('error' not in payload), result=result)

    return wrapper


def post_payload(func):
    """Decorator that extracts POST JSON body and wraps response."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        payload = request.get_json(silent=True) or {}
        result = func(payload)
        print(f"Returned: {result}")
        return jsonify(success=('error' not in payload), result=result)

    return wrapper


def with_dependency(**dependencies):
    """Decorator factory that injects dependencies into route functions."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **{**kwargs, **dependencies})

        return wrapper

    return decorator


class FlaskServer:
    def __init__(self, host="localhost", port=5000):
        self.app = Flask(__name__)
        self.host = host
        self.port = port

    def run(self):
        self.app.run(host=self.host, port=self.port)
