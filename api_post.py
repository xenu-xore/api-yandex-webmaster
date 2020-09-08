# -*- coding: utf-8 -*-
import requests, json


USER_URL = 'https://api.webmaster.yandex.net/v4/user/'
# OAuth-токен пользователя, от имени которого будут выполняться запросы
token = 'input TOKEN'

body = {'input body'}

headers_post = {"Authorization": "OAuth " + token,  # OAuth-токен.
           "Accept-Language": "ru",  # Язык ответных сообщений
           'Content-Type': 'application/json;charset=UTF-8'
           }
headers = {
    "Authorization": "OAuth " + token,
           }



# Выполнение запроса
result = requests.get(USER_URL, headers=headers)


try:
    if result.status_code == 200:
        res = result.json()        
        user_id = res['user_id']
        print('Выполненно с кодом: {}'.format(result.status_code)) 
        print('ID получен') 
        print('Ваш ID: {}'.format(user_id))
        user_id_input = input('Введите ваш ID: ')
        USER_URL_HOSTS = 'https://api.webmaster.yandex.net/v4/user/' + str(user_id_input) + str('/hosts/')        
except:
    if result.status_code != 200 or result.json().get("error", False):
        print("Код ошибки: {}".format(result.status_code))
    else:
        print('Неизвестная ошибка USER_URL')  
               
result_hosts = requests.get(USER_URL_HOSTS, headers=headers) 

try:
    if result_hosts.status_code == 200:
        res_hosts = result_hosts.json()
        print("Доступные host_id")     
        for res_hosts_ in res_hosts["hosts"]:
            res_hosts_up = res_hosts_['host_id']
            print(res_hosts_up)
            
        print('Выполненно с кодом: {}'.format(result_hosts.status_code))          
except:
    if result_hosts.status_code != 200 or result_hosts.json().get("error", False):
        print("Код ошибки: {}".format(result_hosts.status_code))
    else:
        print('Неизвестная ошибка USER_URL_HOSTS')  
        
hosts_input = input('Введите ваш hosts_id {}'.format(result_hosts.url))
result_hosts_input = result_hosts.url + str(hosts_input)
result_hosts_input = requests.get(result_hosts.url + str(hosts_input), headers=headers)

try:
    if result_hosts_input.status_code == 200:        
        result_hosts_input = result_hosts_input.text.split(',')
        print("Основная информация о host_id: {}".format(hosts_input))
        for result_hosts_input_temp in result_hosts_input:
            print(result_hosts_input_temp)
    else:
        
        while result_hosts_input.status_code != 200:
                      
            hosts_input = input('Повторите попытку ввода hosts_id {}'.format(result_hosts.url))            
            result_hosts_input = result_hosts.url + str(hosts_input)                
            result_hosts_input = requests.get(result_hosts.url + str(hosts_input), headers=headers)           
            print('Код ответа: {}'.format(result_hosts_input.status_code))
            
            if result_hosts_input.status_code == 200:
                
                print('Cтатус кода: {}'.format(result_hosts_input.status_code))
                
                result_hosts_input = result_hosts_input.text.split(',')
                for result_hosts_input_err in result_hosts_input:      
                    print(result_hosts_input_err)
                                 
                break
            else:
                pass          
except:        
    pass


while True:
    next_input_1 = input('Продолжите команду {}'.format(result_hosts.url + str(hosts_input)))
    if next_input_1:
        USER_URL_NEXT=result_hosts.url +str(hosts_input)+ str(next_input_1)
  
        # Кодирование тела запроса в JSON
        jsonBody = json.dumps(body)
        result_next_POST = requests.post(USER_URL_NEXT, jsonBody, headers=headers_post)

        try: 
            if result_next_POST.status_code == 201:               
                print("Выполненно с кодом: {}".format(result_next_POST.status_code))
                result_next_POST = result_next_POST.text.split(',')
                for result_next_error in result_next_POST:
                    print(result_next_error)
                    
            else:
                if result_next_POST.status_code != 201:
                    print('Ошибка' + result_next_POST.status_code)
                else:
                    pass
                    
        except:
            print('Неизвесная ошибка')
            print(result_next_POST.text)
            
    else:
        print('Error')                                                        