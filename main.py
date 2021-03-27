import json
import time
from http import client
from urllib.parse import urlencode

from file_manager import FileManager
from mac_generator import mac_generator

REQUEST_HOST = 'www.mercadobitcoin.net'
REQUEST_PATH = '/tapi/v3/'


def post_request():
    try:
        conn = client.HTTPSConnection(REQUEST_HOST)
        conn.request("POST", REQUEST_PATH, params, headers)

        response = conn.getresponse()
        response = response.read()

        response_json = json.loads(response)
        print('status: {}'.format(response_json['status_code']))
        print(json.dumps(response_json, indent=4))
    except ValueError:
        print('API ERROR')
    else:
        conn.close()
        return json


if __name__ == '__main__':
    tapi_info = FileManager.get_tap_user_info()
    tapi_id, tapi_secret = tapi_info['tapi_id'], tapi_info['tapi_secret']
    tapi_method = 'get_account_info'

    tapi_nonce = str(int(time.time()))

    # Parâmetros
    params = {
        'tapi_method': tapi_method,
        'tapi_nonce': tapi_nonce,
    }
    params = urlencode(params)

    # Gerar MAC
    tapi_mac = mac_generator(REQUEST_PATH, params, tapi_secret)

    # Gerar cabeçalho da requisição
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'TAPI-ID': tapi_id,
        'TAPI-MAC': tapi_mac
    }

    # Realizar requisição POST
    post_request()
