import os, httpx
from datetime import datetime, timedelta
from app.models.HistoricoClima import InformacaoDiaTemperatura
from app.service.Clima import Clima
from app.repository.Repository import InfoRepository
infoRepo = InfoRepository()

class ClimaAdvisorService(Clima):
    def __init__(self) -> None:
        self.fonte = 'APIADVISOR'
        self.cidade = 'SAO PAULO'

    async def save_temperatures_predictions(self) -> None:
        current_date = datetime.now()
        self.json = await self._request_forcast()
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
        data_key = data_mais_x.strftime('%Y-%m-%d')
        for dia_info in self.json['data']:
            if dia_info['date'] == data_key:
                dici = {
                        'id_dia': int(data_key.replace('-', '')),
                        'x_dias': x_days,                        
                        'fonte': self.fonte,
                        'cidade': self.cidade
                    }
                if x_days == 0:
                    dici.update({
                        f'temperatura_real_min': dia_info['temperature']['min'],
                        f'temperatura_real_max':  dia_info['temperature']['max'], 
                    })
                else: 
                    dici.update({
                        f'dia_previsao_feita_menos_x': current_date,
                        f'temperatura_min_previsao_feita_menos_x': dia_info['temperature']['min'],
                        f'temperatura_max_previsao_feita_menos_x':  dia_info['temperature']['max'],
                    })
                return InformacaoDiaTemperatura(**dici)
        
        return None
    
    async def _request_forcast(self):
        url = os.getenv("urlAdvisor")
        url = f'{url}/forecast/locale/3477/days/15?token={os.getenv("tokenAdvisor")}'
        async with httpx.AsyncClient() as client:
            resp = await client.get(url)
        if resp.status_code != 200:
            raise Exception("")
        
        return resp.json()

