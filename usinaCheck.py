import telebot
import growattServer

api = growattServer.GrowattApi()
login_response = api.login("username", "password")
device_list = api.device_list("plant_id")
inverter_detail = api.inverter_detail("inverter_id")
inverter_data = api.inverter_data("inverter_id")
plant_list = api.plant_list("plant_id")
dictUsina = {
    'plantName': login_response['data'][0]
    ['plantName'],
    'lostStatus': device_list[0]['lost'],
    'time': inverter_detail['time'],
    'potenciaAtualW': device_list[0]['power'],
    'deviceStatus': device_list[0]['deviceStatus'],
    'eTodayStr': device_list[0]['eTodayStr']
}

"""
deviceStatus
    2 Conectado
    4 Anormal
"""

# Send data to Telegram
bot = telebot.TeleBot("botTokenHere")
chatID = 'chatIdHere'

# Check usina Status
if dictUsina['lostStatus'] == False:
    if dictUsina['potenciaAtualW'] == 0:
        bot.send_message(chatID, '⚠️ *Alerta na usina ⚠️*\n'
                         '*Nome da Usina:* {} \n'
                         '*Horario:* {} \n'
                         '*Potencia Atual:* {}(W) 🔌'.format(
                             dictUsina['plantName'],
                             dictUsina['time'],
                             dictUsina['potenciaAtualW']),
                         parse_mode="Markdown"
                         )
    if dictUsina['deviceStatus'] != 2:
        bot.send_message(chatID, '⚠️ *Alerta na usina ⚠️*\n'
                         '*Nome da Usina:* {} \n'
                         '*Horario:* {} \n'
                         '*Status da conexao:* {} ⚡'.format(
                             dictUsina['plantName'],
                             dictUsina['time'],
                             dictUsina['deviceStatus']),
                         parse_mode="Markdown"
                         )


@bot.message_handler(commands=['detalhePlanta', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Informação da Planta! \n'
                 'Nome da Usina: {} \n'
                 'Geração Hoje: {} \n'
                 'Este mês: {}(kWh) \n'
                 'Status da Conexao: {} \n'
                 'Potência Atual: {}(W) \n'
                 'Ultima atualização: ')


bot.infinity_polling()
