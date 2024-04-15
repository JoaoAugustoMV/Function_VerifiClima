import os, httpx

from datetime import datetime, timedelta
from models.HistoricoClima import InformacaoDiaTemperatura
from repository.Repository import InfoRepository
from service.Clima import Clima

infoRepo = InfoRepository()
class ClimaHGBrasil(Clima):

    def __init__(self) -> None:
        self.fonte = 'HGBrasil'
        self.cidade = 'SAO PAULO'

    async def save_temperatures_predictions(self) -> None:
        self.json = await self._request_forcast()
        current_date = datetime.now()
        infos = [
                self._get_prediction_minus_x(current_date, 5),
                self._get_prediction_minus_x(current_date, 3),
                self._get_prediction_minus_x(current_date, 1),
                self._get_prediction_minus_x(current_date, 0)
                ]
        
        for i in infos:
            if i is not None:
                    self._saveInfo(i)

    def _get_prediction_minus_x(self, current_date, x_days):
        data_mais_x = current_date + timedelta(days=x_days)
        data_key = data_mais_x.strftime('%d/%m')
        for dia_info in self.json['results']['forecast']:
            if dia_info['date'] == data_key:
                id_dia = int(data_mais_x.strftime('%Y-%m-%d').replace('-', '')) 
                dici = {
                        'id_dia': id_dia,
                        'x_dias': x_days,                        
                        'fonte': self.fonte,
                        'cidade': self.cidade,
                        'descricao': dia_info['description']
                    }
                if x_days == 0:
                    dici.update({
                        f'dia_previsao_feita_menos_x': current_date,
                        f'temperatura_real_min': dia_info['min'],
                        f'temperatura_real_max':  dia_info['max'], 
                    })
                else: 
                    dici.update({
                        f'dia_previsao_feita_menos_x': current_date,
                        f'temperatura_min_previsao_feita_menos_x': dia_info['min'],
                        f'temperatura_max_previsao_feita_menos_x':  dia_info['max'],
                    })
                return InformacaoDiaTemperatura(**dici)
        
        return None

    async def _request_forcast(self):
        url = os.getenv("urlHGBrasil")
        url = f'{url}?woeid=455827%20'
        async with httpx.AsyncClient() as client:
            resp = await client.get(url)
        
        if resp.status_code != 200:
            raise Exception("")
        
        return resp.json()