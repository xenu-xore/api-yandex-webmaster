# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, redirect
from requests import post
from urllib.parse import urlencode


# Идентификатор приложения
client_id = 'Input client_id'
# Пароль приложения
client_secret = 'Input client_secret'
# Адрес сервера Яндекс.OAuth
baseurl = 'https://oauth.yandex.ru/'

app = Flask(__name__)


@app.route('/')
def index():
    if request.args.get('code', False):

        print(request.args)
        print(request.data)
        data = {
            'grant_type': 'authorization_code',
            'code': request.args.get('code'),
            'client_id': client_id,
            'client_secret': client_secret
        }
        data = urlencode(data)
     
        return jsonify(post(baseurl + "token", data).json())
        
    else:

        return redirect(baseurl + "authorize?response_type=token&client_id={}".format(client_id))
        
if __name__ == '__main__':
    # Отладочная информация
    # app.debug = True
    print('Open URL for get TOKEN http://127.0.0.1:8000')
    app.run(host='127.0.0.1', port=8000)