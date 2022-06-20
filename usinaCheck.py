import requests
import growattServer

api = growattServer.GrowattApi()
login_response = api.login("username", "password")
device_list = api.device_list(123456)
inverter_detail = api.inverter_detail("NSinversor")

dictUsina = {
    'plantName': login_response['data'][0]
    ['plantName'],
    'lostStatus': device_list[0]['lost'],
    'time': inverter_detail['time'],
    'potenciaAtualW': device_list[0]['power'],
    'deviceStatus': device_list[0]['deviceStatus']
}

# Send data to Telegram


def telegram_sendtext(bot_message):
    bot_token = 'botTokenHere'
    bot_chatID = 'passwordChatID'
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


# Check usina Status
if dictUsina['lostStatus'] == False:
    if dictUsina['potenciaAtualW'] == 0:
        telegram_sendtext(
            "Usina de *{}* apresentando potencia atual *{}(W)* as {}".format(dictUsina['plantName'], dictUsina['potenciaAtualW'], dictUsina['time']))
    if dictUsina['deviceStatus'] not in 2:
        telegram_sendtext(
            "Usina de *{}* apresentando Status *{}* diferente de Conectado as {}".format(
                dictUsina['PlantName'], dictUsina['deviceStatus'], dictUsina['time'])
        )
