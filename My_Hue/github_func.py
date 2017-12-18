import base64
import json
import requests


# Si queremos imprimir los json de respuesta
# de una forma mas agradable a la vista podemos usar
def print_pretty(jsonstring, indent=4, sort_keys=False):
    print(json.dumps(jsonstring, indent=indent, sort_keys=sort_keys))


# Datos de GitHub
credentials = ('rodrigozs','5df96071476b0b8ffb0d57be218089e3ecbad510')
url = "https://api.github.com/repos/rodrigozs/dummy_repo/issues/"

# OBTENER UNA ISSUE
def get_issue(numero_issue):
    url_issue = url + str(numero_issue)
    req = requests.get(url_issue, auth=credentials)
    return req.json()

# PUBLICAR UNA RESPUESTA
def post_comment(numero_issue, comment_txt):
    url_issue = url + str(numero_issue) + '/' + 'comments'
    comment = {'body': comment_txt}
    requests.post(url_issue, data = json.dumps(comment), auth=credentials)
    return

# AGREGAR UNA LABEL A UNA ISSUE
def add_label(numero_issue, label):
    url_labels = url + str(numero_issue) + '/labels'

    # obtenemos la issue correspondiente
    params = get_issue(numero_issue)

    # agregarmos label
    nueva_label = [label]
    requests.post(url_labels, data = json.dumps(nueva_label), auth=credentials)
    return

# CERRAR UNA ISSUE
def close_issue(numero_issue):
    url_issue = url + str(numero_issue)
    state = {'state': 'closed'}
    requests.patch(url_issue, data = json.dumps(state), auth=credentials)
    return

# ABRIR UNA ISSUE
def open_issue(numero_issue):
    url_issue = url + str(numero_issue)
    state = {'state': 'open'}
    requests.patch(url_issue, data = json.dumps(state), auth=credentials)
    return


if __name__ == '__main__':
    close_issue(1)
    req = get_issue(1)
    print_pretty(req)
