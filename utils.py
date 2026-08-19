from unittest import case
import urllib.request
import json


def reloadWcif(compId):
    jsonFile = urllib.request.urlopen(f'https://worldcubeassociation.org/api/v0/competitions/{compId}/wcif/public')
    wcif = json.loads(jsonFile.read())
    groupsMain = []
    groupsSide = []

    for activity in wcif['schedule']['venues'][0]['rooms'][0]['activities']:
        toEnter = []
        if len(activity['childActivities']) == 0:
            toEnter.append(activity)
        else:
            for child in activity['childActivities']:
                toEnter.append(child)
        for child in toEnter:
            groupsMain.append((child['activityCode'], child['startTime']))
    groupsMain.sort(key=lambda x: x[1])

    for activity in wcif['schedule']['venues'][0]['rooms'][2]['activities']:
        toEnter = []
        if len(activity['childActivities']) == 0:
            toEnter.append(activity)
        else:
            for child in activity['childActivities']:
                toEnter.append(child)
        for child in toEnter:
            groupsSide.append((child['activityCode'], child['startTime']))

    groupsSide.sort(key=lambda x: x[1])

    return (groupsMain, groupsSide, wcif)


events = {
    '333': ('3x3', 4),
    '222': ('2x2', 3),
    '444': ('4x4', 3),
    '555': ('5x5', 2),
    '666': ('6x6', 1),
    '777': ('7x7', 1),
    '333bf': ('3BLD', 2),
    '333fm': ('FMC', 1),
    '333oh': ('OH', 3),
    'clock': ('Clock', 2),
    'minx': ('Megaminx', 2),
    'pyram': ('Pyraminx', 3),
    'skewb': ('Skewb', 3),
    'sq1': ('Square-1', 2),
    '444bf': ('4BLD', 1),
    '555bf': ('5BLD', 1),
    '333mbf': ('Multi', 1)
}


def getTexts(activity):
    eventId = activity.split("-")[0]
    if eventId in events:
        return (events[eventId][0], f'Round {activity.split("-")[1][1:]}', f'Group {activity.split("-")[2][1:]}')

    match activity.split("-")[1]:
        case 'checkin':
            return ('Check-in', '', '')
        case 'lunch':
            return ('Lunch', '', '')
        case 'misc':
            return ('Coupe de France', '', '')
        case 'multi':
            return ('Dropoff multi', '', '')
        case _:
            return ('', '', '')
