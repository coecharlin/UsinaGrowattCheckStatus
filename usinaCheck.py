import telebot
import growattServer

api = growattServer.GrowattApi()
login_response = api.login("Caroline Fernandes", "Lightenergy")
device_list = api.device_list(644575)
inverter_detail = api.inverter_detail("DYH0B0601M")
inverter_data = api.inverter_data("DYH0B0601M")
plant_list = api.plant_list(644575)
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
    1 Esperando
"""


# Send data to Telegram
bot = telebot.TeleBot("1432121388:AAFd_UVoDCSFmKb7uiD3EUzor8q4djHIPVA")
chatID = '1206596200'

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
def send_message(message):
    bot.reply_to(message, 'Informação da Planta! \n'
                 'Nome da Usina: {} \n'
                 'Geração Hoje: {} \n'
                 'Este mês: {}(kWh) \n'
                 'Status da Conexao: {} \n'
                 'Potência Atual: {}(W) \n'
                 'Ultima atualização: ')


# bot.infinity_polling()
