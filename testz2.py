import os
import json
import requests


def makeRequest(type, cuid, data, settings):
    server = os.getenv('api2_server')
    url = "{server}{type}/{uuid}/{cuid}".format(server=server,
                                                type=type,
                                                uuid=settings['uuid'],
                                                cuid=cuid if cuid != '' else '',
                                                )
    payload = json.dumps(data)
    result = requests.post(url, payload)
    if result == '':
        return None
    return result
