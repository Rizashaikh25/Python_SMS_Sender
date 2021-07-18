"""
Python project to send sms tusing API of Fast2SMS
install package requests (To request any api)
json package is bt default availabe
"""
import requests
import json

def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulkV2'
    params = {
        'authorization': 'UcOJzEpbAx5ZHvlkCwnfyhd9FS8t7j6u30XqD2MiWRmGoVLY1N9k1qc2tLigKx3y80IH4QFXvbPUhaRV',
        'sender_id':'CHKSMS',
        'language': 'English',
        'message': message,
        'route' : 'q',
        'numbers': number
    }

    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)
    return dic.get('return')
send_sms(int(input("Enter Number")), input("Enter Message"))