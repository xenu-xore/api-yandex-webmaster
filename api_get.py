# -*- coding: utf-8 -*-
import requests

#  Адрес сервиса
USER_URL = 'https://api.webmaster.yandex.net/v4/user/'

# OAuth-токен пользователя
TOKEN = 'Input TOKEN'

#  Создание HTTP-заголовков GET запроса
headers = {
    "Authorization": "OAuth " + TOKEN,
           }



#Резултат выполненной
FILE = "result_url.json"
FILE_1 = "resultURL.txt"
FILE_2 = "resultQueries.txt"
FILE_3 = "result-queries.json"                                    

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
        
        #date_from = input("Ключи от Дата: 2019-08-20: ")
        #order_by = input("Клики или показы: TOTAL_CLICKS: ")
        #query_indicator = input("Показы: TOTAL_CLICKS: ")
        #date_to = input("Ключи до Дата: 2020-08-26: ")
               
        #param={
        #     "date_from": date_from,            
        #     "order_by": order_by,    
        #     "query_indicator": query_indicator,       
        #     "date_to": date_to,                      
        #    }
        
        #result_next = requests.get(USER_URL_NEXT, headers=headers, params=param)
        
        result_next = requests.get(USER_URL_NEXT, headers=headers)

        try:
            #Под ключевые слова список
            if result_next.status_code == 200:
                res_next_param = result_next.json()
                file_open_2 = open(FILE_2, "w", encoding='utf8') 
                next_param = res_next_param['count']
                print("--------------------------------------------------------TXT---------------------------------------------------------") 
                for res_next_param_queries_key in res_next_param["queries"]:
                    res_next_param_queries_up = res_next_param_queries_key['query_text'] 
                    res_next_param_queries_up_indicators = res_next_param_queries_key['indicators']['TOTAL_CLICKS']                
                    print(res_next_param_queries_up) 
#                    print('Метрика: {}'.format(res_next_param_queries_up_indicators))                                    
#                print('Выполненно с кодом: {}'.format(result_next.status_code))
                    file_open_2.write(res_next_param_queries_up + '\n')
                file_open_2.close()                 
                print('Выполненно с кодом: {}'.format(result_next.status_code))                  
                print('Всего ключей: {}'.format(next_param))
                
            #Ключевые слова в JSON           
                print("--------------------------------------------------------JSON---------------------------------------------------------")
                
                #Запись в файл result.json
                res_next_param = result_next.text             
                print(res_next_param)
                
                file_open = open(FILE_3, "w", encoding='utf8')                
                for res_next_param_queries in res_next_param:
                    file_open.write(res_next_param_queries)
                file_open.close()
                
            else:
                next_param_error = res_next_param["error_message"]
                print('Ошибка ввода: {}'.format(next_param_error))
                
                                        
        except:
                        
            if result_next.status_code != 200 or result_next.json().get("error", False):               
                print("Код ошибки: {}".format(result_next.status_code))
                result_next = result_next.text.split(',')
                for result_next_error in result_next:
                    print(result_next_error)
                print('Неправильно введена команда. Пройдите по ссылке для изучение доступных команд https://yandex.ru/dev/webmaster/doc/dg/concepts/getting-started-docpage/')

            else:
                pass
            
        #URL список
        try:
            if result_next.status_code == 200:
                res_next_param = result_next.json()
                file_open_1 = open(FILE_1, "w", encoding='utf8')  
                print("--------------------------------------------------------TXT---------------------------------------------------------") 
                for res_next_param_queries_key in res_next_param["samples"]:
                    res_next_param_queries_up = res_next_param_queries_key['url'] 
                    res_next_param_queries_up_indicators = res_next_param_queries_key['status']                                 
                    print(res_next_param_queries_up)
                    file_open_1.write(res_next_param_queries_up + '\n')
                file_open_1.close()   
                             
                #URL в JSON
                print("--------------------------------------------------------JSON---------------------------------------------------------")
                                    
                res_next_param = result_next.text             
                print(res_next_param)
                
                file_open = open(FILE, "w", encoding='utf8')                
                for res_next_param_queries in res_next_param:
                    file_open.write(res_next_param_queries)
                file_open.close()
                
            else:
                next_param_error = res_next_param["error_message"]
                print('Ошибка ввода: {}'.format(next_param_error))
                
                                        
        except:            
            if result_next.status_code != 200 or result_next.json().get("error", False):               
                print("Код ошибки: {}".format(result_next.status_code))
                result_next = result_next.text.split(',')
                for result_next_error in result_next:
                    print(result_next_error)
                print('Неправильно введена команда. Пройдите по ссылке для изучение доступных команд https://yandex.ru/dev/webmaster/doc/dg/concepts/getting-started-docpage/')

            else:
                pass
                                    
    else:
        print('Неизвестная ошибка')