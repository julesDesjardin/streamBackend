import utils

from FlaskServer import post_payload, with_dependency


def setupPageRoutes(app, obs, companion):
    """Register setupPage routes on the Flask app."""

    scheduleIndices = {
        "main": 0,
        "side": 0
    }

    COMP_ID = "FrenchChampionship2026"

    groupsMain, groupsSide, wcif = utils.reloadWcif(COMP_ID)

    groups = {
        "main": groupsMain,
        "side": groupsSide
    }
    row = {
        "main": 2,
        "side": 3
    }

    @app.route("/updateSchedule", methods=["POST"])
    @post_payload
    @with_dependency(obs=obs, companion=companion)
    def updateSchedule(payload, obs, companion):
        print("Received updateSchedule")
        room = payload.get("room")
        increment = payload.get("increment")
        if room is None:
            return {"error": "Missing 'room' parameter"}
        if room not in ["main", "side"]:
            return {"error": "Invalid 'room' parameter. Must be 'main' or 'side'"}
        if increment is None:
            return {"error": "Missing 'increment' parameter"}
        if increment not in ["-1", "+1"]:
            return {"error": "Invalid 'increment' parameter. Must be '-1' or '+1'"}

        print(f"Updating schedule for room {room} with increment {increment}")

        if not (scheduleIndices[room] == 0 and increment == "-1") and not (scheduleIndices[room] == len(groups[room]) - 1 and increment == "+1"):
            scheduleIndices[room] += int(increment)

        event, round, group = utils.getTexts(groups[room][scheduleIndices[room]][0])

        companion.setButton(companion.Page.SETUP, row[room], 0, event)
        companion.setButton(companion.Page.SETUP, row[room], 1, round)
        companion.setButton(companion.Page.SETUP, row[room], 2, group)

        if scheduleIndices[room] + 1 >= len(groups[room]):
            nextEvent, nextRound, nextGroup = "End", "", ""
        else:
            nextEvent, nextRound, nextGroup = utils.getTexts(groups[room][scheduleIndices[room] + 1][0])

        companion.setButton(companion.Page.SETUP, row[room], 3, nextEvent)
        companion.setButton(companion.Page.SETUP, row[room], 4, nextRound)
        companion.setButton(companion.Page.SETUP, row[room], 5, nextGroup)

        return {"room": room, "increment": increment}
