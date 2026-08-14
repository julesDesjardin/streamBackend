from flask import Flask, request, jsonify
from obsws_python import ReqClient

from FlaskServer import FlaskServer


def helloWorldGet(payload):
    print(payload['message'])
    return f"Hello, {payload['message']}!"


def helloWorldPost(payload):
    print(payload['message'])
    return f"Hello, {payload['message']}!"


def main():
    flaskServer = FlaskServer()

    flaskServer.addGetRoute("/helloGet", helloWorldGet)
    flaskServer.addPostRoute("/helloPost", helloWorldPost)

    flaskServer.run()


if __name__ == "__main__":
    main()
