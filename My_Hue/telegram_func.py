import json
import requests


# Datos importantes
token = "bot463324909:AAHeufMxi_-_Px0mcTa1ywsCqcG8Gt-2Yo0"
url = "https://api.telegram.org/"+token+"/"
header = {'content-Type': 'application/json'}

def send_msg(chat_id, text):
    form = {'chat_id': chat_id, 'text': text}
    requests.post(url + 'sendMessage', headers=header, data=json.dumps(form))
    return "!"

def set_webhook(token):
    # Webhook
    url = "https://api.telegram.org/"+token+"/setWebhook"
    header = {'content-Type': 'application/json'}
    app_heroku = {"url":'https://rodrigozs-heroku-app.herokuapp.com/api'}
    r = requests.post(url, headers=header, data=json.dumps(app_heroku))
    return r

def del_webhook(token):
    url = "https://api.telegram.org/"+token+"/setWebhook"
    header = {'content-Type': 'application/json'}
    r = requests.put(url, headers=header)
    return r


if __name__ == '__main__':
    # Webhook
    wh = set_webhook(token)
    print(r.json())
