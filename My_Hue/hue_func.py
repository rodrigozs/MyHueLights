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
        r = requests.get(url_get)
        return r.json()

    else:
        url_get = url + '/lights' + '/' + light_name
        r = requests.get(url_get)
        return r.json()


def turn_on(light_name):
    if light_name == 'all':
        pass

    else:
        url_turn_on = url + '/lights' + '/' + light_name + '/' + 'state'
        form = {"on":"true", "sat":254, "bri":254,"hue":10000}
        r = requests.put(url_turn_on, headers=header, data = json.dumps(form))
        return r.json()


if __name__ == '__main__':
    r = turn_on('7')
    print_pretty(r.json())
