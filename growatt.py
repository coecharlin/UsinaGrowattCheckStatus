import requests
import json


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
