#import bot
import base64
import json
import requests
import flask
import os
import telegram_func as telegram
import hue_func as hue


app = flask.Flask(__name__)

@app.route('/api', methods = ['POST', 'GET', 'PUT'])
def api_get():
    req = flask.request.get_json()

    # Mensaje de Telegram
    mensaje = req['message']['text']
    chat_id = req['message']['chat']['id']

    # obtenemos el comando al encontrar el primer espacio
    ind_comando = mensaje.find(' ')
    comando = mensaje[:ind_comando]
    resto_mensaje = mensaje[ind_comando + 1 :]

    print('comando:{} , resto_mensaje: {}'.format(comando, resto_mensaje))

    # comandos de Telegram
    if comando == '/info':
        print('comando == info: True')
        light_num = str(resto_mensaje.strip(' '))
        print('light_num: {} is number? {}'.format(light_num,light_num.isdigit()))

        if light_num.isdigit():
            info = hue.get_light(light_num)
            name = info['name']
            state = 'ON' if info['state']['on'] == True else 'OFF'
            text = '''[#{0} - {1}: is {2}] \n\n'''.format(light_num, name, state)
            print('text: {}'.format(text))
            telegram.send_msg(chat_id, text)
            return "!"

        elif light_num == 'all':
            pass
            return '!'

        else:
            text = '''Lo siento, pero la ampolleta {0} no existe.
            Intenta de nuevo'''.format(light_num)
            telegram.send_msg(chat_id, text)
            return "!"

    elif comando == '/turn_on':
        light_num = str(resto_mensaje.strip(' '))

        if light_num.isdigit():
            # turn on the light
            hue.turn_on(light_num)

            # show the
            info = hue.get_light(light_num)
            name = info['name']
            state = 'ON' if info['state']['on'] == True else 'OFF'
            text = '''[#{0} - {1}: now is {2}] \n\n'''.format(light_num, name, state)

            telegram.send_msg(chat_id, text)
            return "!"


    elif comando == '/label':
        pass

    elif comando == '/close':
        pass

    else:
        text = 'Lo siento, no te entendi bien'
        telegram.send_msg(chat_id, text)
        return "!"

if __name__ == '__main__':
    app.run()
