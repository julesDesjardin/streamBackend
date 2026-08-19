from CompanionHandler import CompanionHandler
from FlaskServer import FlaskServer
from mainPage import mainPageRoutes
from OBSHandler import OBSHandler
from setupPage import setupPageRoutes


def main():
    flaskServerInst = FlaskServer()
    obs = OBSHandler()
    companion = CompanionHandler("127.0.0.1", 8000)

    # Register feature routes
    mainPageRoutes(flaskServerInst.app, obs)
    setupPageRoutes(flaskServerInst.app, obs, companion)

    flaskServerInst.run()


if __name__ == "__main__":
    main()
