import json
import requests
import telebot


session = requests.Session()


class GrowattApi:

    server_url = 'http://server.growatt.com/login/toSharePlant/85AF9942EEC03C351D39D9E5DBE387F208D6904CE2151AD38FF249B3786234B9A5ECCF246BCB86447FD92A7E26F3270C'

    def getWeatherByPlantId(self, plantId):
        session.get(self.server_url)
        response = session.post(
            'http://server.growatt.com/index/getWeatherByPlantId',
            params={
                'plantId': plantId
            })
        data = json.loads(response.content.decode('utf-8'))
        return data

    def getPlantData(self, plantId):
        session.get(self.server_url)
        response = session.post(
            'http://server.growatt.com/panel/getPlantData',
            params={
                'plantId': plantId
            })
        data = json.loads(response.content.decode('utf-8'))
        return data

    def getInvDayChart(self, plantId, date):
        session.get(self.server_url)
        response = session.post(
            'http://server.growatt.com/panel/inv/getInvDayChart',
            params={
                'date': date,
                'plantId': plantId
            })
        data = json.loads(response.content.decode('utf-8'))
        return data

    def getInvMonthChart(self, plantId, date):
        session.get(self.server_url)
        response = session.post(
            'http://server.growatt.com/panel/inv/getInvMonthChart',
            params={
                'date': date,
                'plantId': plantId
            })
        data = json.loads(response.content.decode('utf-8'))
        return data

    def getInvYearChart(self, plantId, year):
        session.get(self.server_url)
        response = session.post(
            'http://server.growatt.com/panel/inv/getInvYearChart',
            params={
                'year': year,
                'plantId': plantId
            })
        data = json.loads(response.content.decode('utf-8'))
        return data

    def getInvTotalChart(self, plantId, year):
        session.get(self.server_url)
        response = session.post(
            'http://server.growatt.com/panel/inv/getInvTotalChart',
            params={
                'year': year,
                'plantId': plantId
            })
        data = json.loads(response.content.decode('utf-8'))
        return data

    def getInvTotalData(self, plantId):
        session.get(self.server_url)
        response = session.post(
            'http://server.growatt.com/panel/inv/getInvTotalData',
            params={
                'plantId': plantId
            })
        data = json.loads(response.content.decode('utf-8'))
        return data

    def getInverterList2(self, plantId):
        session.get(self.server_url)
        response = session.post(
            'http://server.growatt.com/device/getInverterList2',
            params={
                'invSn': '',
                'plantId': plantId,
                'currPage': 1
            })
        data = json.loads(response.content.decode('utf-8'))
        return data

    def getPlantTotalData(self, plantId):
        session.get(self.server_url)
        response = session.post(
            'http://server.growatt.com/device/getPlantTotalData',
            params={
                'plantId': plantId
            })
        data = json.loads(response.content.decode('utf-8'))
        return data

    def getDeviceInfo(self, plantId, deviceTypeName, sn):
        session.get(self.server_url)
        response = session.post(
            'http://server.growatt.com/panel/getDeviceInfo',
            params={
                'plantId': plantId,
                'deviceTypeName': deviceTypeName,
                'sn': sn
            })
        data = json.loads(response.content.decode('utf-8'))
        return data


api = GrowattApi()

getPlantData = api.getPlantData(644575)
getInvTotalData = api.getInvTotalData(644575)
getPlantTotalData = api.getPlantTotalData(644575)
getInverterList2 = api.getInverterList2(644575)
getDeviceInfo = api.getDeviceInfo(644575, 'datalog', 'RID0B040Z1')

status = int(getInverterList2['datas'][0]['status'])
match status:
    case 1:
        status = "1-Conectado"
    case 2:
        status = "2-Aguardando"
    case 3:
        status = "3-Apresentando problemas"
    case 4:
        status = "4-Keep"
    case -1:
        status = "Desconectado"


simSignal = int(getDeviceInfo['obj']['simSignal'])
if simSignal <= 0 and simSignal >= -50:
    simSignal = 'Excelente(' + str(simSignal)+')'
elif simSignal <= -51 and simSignal >= -75:
    simSignal = 'Bom(' + str(simSignal)+')'
elif simSignal <= -76 and simSignal >= -113:
    simSignal = 'Fraco(' + str(simSignal)+')'
else:
    "Erro ao receber os dados"


dictGrowattApi = {
    'co2': getPlantData['obj']['co2'],
    'tree': getPlantData['obj']['tree'],
    'coal': getPlantData['obj']['coal'],
    'eToday': getInvTotalData['obj']['eToday'],
    'eMonth': getPlantTotalData['obj']['eMonth'],
    'eTotal': getInvTotalData['obj']['eTotal'],
    'mToday': getInvTotalData['obj']['mUnitText'] + " " + getInvTotalData['obj']['mToday'],
    'mMonth': getInvTotalData['obj']['mUnitText'] + " " + getPlantTotalData['obj']['mMonth'],
    'mTotal': getInvTotalData['obj']['mUnitText'] + " " + getInvTotalData['obj']['mTotal'],
    'lastUpdateTime': getInverterList2['datas'][0]['lastUpdateTime'],
    'deviceModel': getInverterList2['datas'][0]['deviceModel'],
    'nominalPower': getInverterList2['datas'][0]['nominalPower'],
    'pac': getInverterList2['datas'][0]['pac'],
    'sn': getInverterList2['datas'][0]['sn'],
    'plantName': getInverterList2['datas'][0]['plantName'],
    'status': status,
    'ipAndPort': getDeviceInfo['obj']['ipAndPort'],
    'deviceType': getDeviceInfo['obj']['deviceType'],
    'simSignal': simSignal,
    'lost': getInverterList2['datas'][0]['lost']
}

# Send data to Telegram
bot = telebot.TeleBot('1432121388:AAFd_UVoDCSFmKb7uiD3EUzor8q4djHIPVA')
chatID = '1206596200'


@bot.message_handler(commands=['contribuicaosocial'])
def send_message(message):
    bot.reply_to(message,
                 'Nome da Usina: {} \n'
                 'CO₂ reduzido: {} \n'
                 'Árvores salvas: {} \n'
                 'Economia carvão: {} \n'
                 'Ultima atualização: {}'.format(
                     dictGrowattApi['plantName'],
                     dictGrowattApi['co2'],
                     dictGrowattApi['tree'],
                     dictGrowattApi['coal'],
                     dictGrowattApi['lastUpdateTime']
                 ))


@bot.message_handler(commands=['resumo'])
def send_message(message):
    bot.reply_to(message,
                 'Nome da Usina: {} \n'
                 '\n'
                 'Energia Hoje: {}(kWh) \n'
                 'Rendimento Hoje: {} \n'
                 '\n'
                 'Energia Mensal: {}(kWh) \n'
                 'Rendimento Mensal: R$ {} \n'
                 '\n'
                 'Energia Total: {}(kWh) \n'
                 'Rendimento Total: {} \n'
                 '\n'
                 'Ultima atualização: {}'.format(
                     dictGrowattApi['plantName'],
                     dictGrowattApi['eToday'],
                     dictGrowattApi['mToday'],
                     dictGrowattApi['eMonth'],
                     dictGrowattApi['mMonth'],
                     dictGrowattApi['eTotal'],
                     dictGrowattApi['mTotal'],
                     dictGrowattApi['lastUpdateTime']
                 ))


@bot.message_handler(commands=['status'])
def send_message(message):
    bot.reply_to(message, 'Nome da Usina: {} \n'
                 'Potencia Atual: {} (W) \n'
                 'Geracao Hoje: {} (kWh) \n'
                 'Status da conexão: {} \n'
                 'Qualidade da conexão: {} \n'
                 'Ultima atualização: {}'.format(
                     dictGrowattApi['plantName'],
                     dictGrowattApi['pac'],
                     dictGrowattApi['eToday'],
                     dictGrowattApi['status'],
                     dictGrowattApi['simSignal'],
                     dictGrowattApi['lastUpdateTime']
                 ))


def notificationPotenciaZero():
    bot.send_message(chatID, 'Nome da Usina: {} \n'
                     'Potencia Atual: {} (W) \n'
                     'Geracao Hoje: {} (kWh) \n'
                     'Status da conexão: {} \n'
                     'Qualidade da conexão: {} \n'
                     'Ultima atualização: {}'.format(
                         dictGrowattApi['plantName'],
                         dictGrowattApi['pac'],
                         dictGrowattApi['eToday'],
                         dictGrowattApi['status'],
                         dictGrowattApi['simSignal'],
                         dictGrowattApi['lastUpdateTime']
                     ))


def notificationStatus():
    bot.send_message(chatID, 'Nome da Usina: {} \n'
                     'Potencia Atual: {} (W) \n'
                     'Geracao Hoje: {} (kWh) \n'
                     'Status da conexão: {} \n'
                     'Qualidade da conexão: {} \n'
                     'Ultima atualização: {}'.format(
                         dictGrowattApi['plantName'],
                         dictGrowattApi['pac'],
                         dictGrowattApi['eToday'],
                         dictGrowattApi['status'],
                         dictGrowattApi['simSignal'],
                         dictGrowattApi['lastUpdateTime']
                     ))


if dictGrowattApi['lost'] == False:
    if dictGrowattApi['pac'] == 0:
        notificationPotenciaZero()
    if dictGrowattApi['status'] != "1-Conectado":
        notificationStatus()

bot.infinity_polling()
