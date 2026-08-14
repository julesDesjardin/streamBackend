from flask import Flask, request, jsonify


class FlaskServer:
    def __init__(self, host="localhost", port=5000):
        self.app = Flask(__name__)
        self.host = host
        self.port = port

    def run(self):
        self.app.run(host=self.host, port=self.port)

    def getWrapper(self, func):
        def internalGetWrapper():
            payload = request.args.to_dict()

            return jsonify(
                success=True,
                result=func(payload)
            )

        return internalGetWrapper

    def addGetRoute(self, route, func):
        self.app.add_url_rule(route, view_func=self.getWrapper(func), methods=["GET"])

    def postWrapper(self, func):
        def internalPostWrapper():
            payload = request.get_json()

            return jsonify(
                success=True,
                result=func(payload)
            )

        return internalPostWrapper

    def addPostRoute(self, route, func):
        self.app.add_url_rule(route, view_func=self.postWrapper(func), methods=["POST"])
