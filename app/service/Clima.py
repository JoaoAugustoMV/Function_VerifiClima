from abc import ABC, abstractmethod
from datetime import datetime
from repository.Repository import InfoRepository

from models.HistoricoClima import InformacaoDiaTemperatura
infoRepo = InfoRepository()
class Clima(ABC):
    
    @abstractmethod
    def save_temperatures_predictions(self):
        pass

    @abstractmethod
    def _get_prediction_minus_x(self, current_date: datetime, x_days: int):
        pass

    @abstractmethod
    def _request_forcast(self):
        pass
            
    def _saveInfo(self, info: InformacaoDiaTemperatura):
        infoRepo.insertInfo(info)
