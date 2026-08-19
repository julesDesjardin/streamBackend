from obsws_python import ReqClient
import requests
from enum import IntEnum


class CompanionHandler:
    class Page(IntEnum):
        CROP_PTZ = 1
        CROP_PTZ_CHOOSE_STATION = 2
        OTHER = 3
        SET_COMPETITOR_FINAL = 4
        SET_STATION_FINAL = 5
        STATION_FINAL_RECAP = 6
        COMPETITOR_RECAP = 7
        SETUP = 8
        CHOOSE_COMPETITOR = 9
        CHOOSE_STATION_FINAL = 10
        CHOOSE_STATION = 11
        MAIN = 12

    def __init__(self, ip, port):

        self.COMPANION = f"http://{ip}:{port}"

    def setButton(self, page, buttonRow, buttonCol, text, color=None):
        payload = {
            "text": text,
        }
        if color is not None:
            payload["bgcolor"] = color
        print(f'{self.COMPANION}/api/location/{page}/{buttonRow}/{buttonCol}/style')
        print(payload)
        requests.post(f'{self.COMPANION}/api/location/{page}/{buttonRow}/{buttonCol}/style',
                      json=payload)
