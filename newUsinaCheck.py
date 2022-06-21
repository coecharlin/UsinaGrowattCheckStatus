from datetime import datetime
import json
from urllib import response
import requests
import telebot


session = requests.Session()


class GrowattApi:

    server_url = 'http://server.growatt.com/login'

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

getPlantData = api.getPlantData(plantId)
dictGetPlantData = {
    'co2': getPlantData['obj']['co2'],
    'tree': getPlantData['obj']['tree'],
    'coal': getPlantData['obj']['coal']
}

getInvTotalData = api.getInvTotalData(plantId)
getPlantTotalData = api.getPlantTotalData(plantId)
dictTotalData = {
    'eToday': getInvTotalData['obj']['eToday'],
    'eMonth': getPlantTotalData['obj']['eMonth'],
    'eTotal': getInvTotalData['obj']['eTotal'],
    'mToday': getInvTotalData['obj']['mUnitText'] + " " + getInvTotalData['obj']['mToday'],
    'mMonth': getInvTotalData['obj']['mUnitText'] + " " + getPlantTotalData['obj']['mMonth'],
    'mTotal': getInvTotalData['obj']['mUnitText'] + " " + getInvTotalData['obj']['mTotal']
}

getInverterList2 = api.getInverterList2(plantId)
dictGetInverterList2 = {
    'lastUpdateTime': getInverterList2['datas'][0]['lastUpdateTime'],
    'deviceModel': getInverterList2['datas'][0]['deviceModel'],
    'nominalPower': getInverterList2['datas'][0]['nominalPower'],
    'pac': getInverterList2['datas'][0]['pac'],
    'sn': getInverterList2['datas'][0]['sn'],
    'plantName': getInverterList2['datas'][0]['plantName'],
    'status': getInverterList2['datas'][0]['status'],
}

getDeviceInfo = api.getDeviceInfo(plantId, 'datalog', 'snDevice0')
dictGetDeviceInfo = {
    'ipAndPort': getDeviceInfo['obj']['ipAndPort'],
    'deviceType': getDeviceInfo['obj']['deviceType'],
    'simSignal': getDeviceInfo['obj']['simSignal']
}

# Send data to Telegram
bot = telebot.TeleBot("botTokenHere")
chatID = 'chatIdHere'


@bot.message_handler(commands=['contribuicaoSocial'])
def send_message(message):
    bot.reply_to(message, 'Contribuição social \n'
                 'Nome da Usina: {} \n'
                 'CO₂ reduzido: {} \n'
                 'Árvores salvas: {}(kWh) \n'
                 'Economia carvão: {} \n'
                 'Ultima atualização: {}'.format(
                     dictGetInverterList2['plantName'],
                     dictTotalData['co2'],
                     dictTotalData['tree'],
                     dictTotalData['coal'],
                     dictTotalData['lastUpdateTime']
                 ))


@bot.message_handler(commands=['resumo'])
def send_message(message):
    bot.reply_to(message, 'Resumo \n'
                 'Nome da Usina: {} \n'
                 'Energia Hoje: {}(kWh) \n'
                 'Rendimento Hoje: {} \n'
                 '\n'
                 'Energia Mensal: {}(kWh)'
                 'Rendimento Mensal: R$ {}'
                 '\n'
                 'Energia Total: {}(kWh) \n'
                 'Rendimento Total: {} \n'
                 'Ultima atualização: {}'.format(
                     dictGetInverterList2['plantName'],
                     dictTotalData['eToday'],
                     dictTotalData['mToday'],
                     dictTotalData['eMonth'],
                     dictTotalData['mMonth'],
                     dictTotalData['eTotal'],
                     dictTotalData['mTotal'],
                     dictGetInverterList2['lastUpdateTime']
                 ))


@bot.message_handler(commands=['status'])
def send_message(message):
    bot.reply_to(message, 'Contribuição social \n'
                 'Nome da Usina: {} \n'
                 'CO₂ reduzido: {} \n'
                 'Árvores salvas: {}(kWh) \n'
                 'Economia carvão: {} \n'
                 'Ultima atualização: {}'.format(
                     dictGetInverterList2['plantName'],
                     dictTotalData['co2'],
                     dictTotalData['tree'],
                     dictTotalData['coal'],
                     dictTotalData['lastUpdateTime']
                 ))
