from FlaskServer import FlaskServer, get_payload, post_payload
from mainPage import mainPageRoutes
from OBSHandler import OBSHandler


def main():
    flaskServerInst = FlaskServer()
    obs = OBSHandler()

    # Register feature routes
    mainPageRoutes(flaskServerInst.app, obs)

    flaskServerInst.run()


if __name__ == "__main__":
    main()
