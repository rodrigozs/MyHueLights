#import bot
import base64
import json
import requests
import flask
import os
import telegram_func as telegram
import hue_func as hue


app = flask.Flask(__name__)

@app.route('/api', methods = ['POST', 'GET', 'PATCH'])
def api_get():
    req = flask.request.get_json()

    # Mensaje de Telegram
    mensaje = req['message']['text']
    chat_id = req['message']['chat']['id']

    # obtenemos el comando al encontrar el primer espacio
    ind_comando = mensaje.find(' ')
    comando = mensaje[:ind_comando]
    resto_mensaje = mensaje[ind_comando + 1 :]

    # comandos de Telegram
    if comando == '/get':
        light_num = resto_mensaje.strip(' ')

        if light_num.isdigit() or light_num == 'all':
            info = hue.get(light_num)

            # Obtenemos datos
            lights = info.keys()
            for light in lights:
                name = info[light]['name']
                state = 'ON' if info[light]['state']['on'] == 'true' else 'OFF'
                text = '''
                [#{0} - {1}: {2}]

                '''.format(light, name, state)

                telegram.send_msg(chat_id, text)
            return "!"

        else:
            text = '''Lo siento, pero la ampolleta {} no existe.
                    'Intenta de nuevo'''.format(light_num)
            telegram.send_msg(chat_id, text)
            return "!"

    elif comando == '/post':
        ind_num_issue = resto_mensaje.find(' ')
        num_issue = resto_mensaje[: ind_num_issue]
        respuesta = resto_mensaje[ind_num_issue + 1 :]

        if num_issue.isdigit():
            github.post_comment(num_issue, respuesta)
            issue = github.get_issue(num_issue)

            # Obtenemos datos
            autor = issue['user']['login']
            num_issue = issue['number']
            titulo = issue['title']
            link_issue = issue['url']

            text = '''
            [{0}] \n\n[#{1} - {2}] \n\nNuevo comentario: \n\n{3} \n\n[Link: {4}]

            '''.format(autor, num_issue, titulo, respuesta, link_issue)

            telegram.send_msg(chat_id, text)
            return "!"

        else:
            text = 'El numero de la issue debe tener exclusivamente numeros'
            telegram.send_msg(chat_id, text)
            return "!"

    elif comando == '/label':
        ind_num_issue = resto_mensaje.find(' ')
        num_issue = resto_mensaje[: ind_num_issue]
        label = resto_mensaje[ind_num_issue + 1 :]

        if num_issue.isdigit():
            github.add_label(num_issue, label)
            issue = github.get_issue(num_issue)

            # Obtenemos datos
            autor = issue['user']['login']
            num_issue = issue['number']
            titulo = issue['title']
            link_issue = issue['url']

            text = '''
            [{0}] \n\n[#{1} - {2}] \n\nNueva Label: {3} \n\n[Link: {4}]

            '''.format(autor, num_issue, titulo, label, link_issue)

            telegram.send_msg(chat_id, text)
            return "!"

        else:
            text = 'El numero de la issue debe tener exclusivamente numeros'
            telegram.send_msg(chat_id, text)
            return "!"

    elif comando == '/close':
        num_issue = resto_mensaje
        print(num_issue)
        print(type(num_issue))

        if num_issue.isdigit():
            issue = github.get_issue(num_issue)

            # Obtenemos datos
            autor = issue['user']['login']
            num_issue = issue['number']
            titulo = issue['title']
            link_issue = issue['url']

            text = '''
            [{0}] \n\n[#{1} - {2}] \n\n- ISSUE CERRADA - \n\n[Link: {3}]

            '''.format(autor, num_issue, titulo, link_issue)

            # Cerramos
            github.close_issue(num_issue)

            telegram.send_msg(chat_id, text)
            return "!"

        else:
            text = 'El numero de la issue debe tener exclusivamente numeros'
            telegram.send_msg(chat_id, text)
            return "!"

    else:
        text = 'Lo siento, no te entendi bien'
        telegram.send_msg(chat_id, text)
        return "!"

if __name__ == '__main__':
    app.run()
