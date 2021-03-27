import hashlib
import hmac


def mac_generator(request_path: str, params: str, tapi_secret: str):
    params_string = request_path + '?' + params
    H = hmac.new(bytes(tapi_secret, encoding='utf8'), digestmod=hashlib.sha512)
    H.update(params_string.encode('utf-8'))
    tapi_mac = H.hexdigest()
    return tapi_mac
