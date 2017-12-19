import json
import requests

header = {'content-Type': 'application/json'}
username = "ahHeS5SJrUdaMWqdiCVSgZ4uedSOsnitjERJBbbO"
bridge_ip = "192.168.0.10"
url = 'http://' + bridge_ip + '/api' + '/' + username

def print_pretty(jsonstring, indent=4, sort_keys=False):
    print(json.dumps(jsonstring, indent=indent, sort_keys=sort_keys))

def get_light(light_name):
    if light_name == 'all':
        url_get = url + '/lights'
        req = requests.get(url_get)
        return req.json()

    else:
        url_get = url + '/lights' + '/' + light_name
        req = requests.get(url_get)
        return req.json()


def turn_on(light_name):
    if light_name == 'all':
        return

    else:
        url_turn_on = url + '/lights' + '/' + light_name + '/' + 'state'
        form = {"on":True}
        req = requests.put(url_turn_on, headers=header, data = json.dumps(form))
        return req.json()


def turn_off(light_name):
    if light_name == 'all':
        return

    else:
        url_turn_on = url + '/lights' + '/' + light_name + '/' + 'state'
        form = {"on":False}
        req = requests.put(url_turn_on, headers=header, data = json.dumps(form))
        return req.json()


if __name__ == '__main__':
    req = 'On' if get_light('7')['state']['on'] == True else 'False'
    print_pretty(req)
