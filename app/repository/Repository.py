import os
from sqlalchemy import create_engine, insert, select
from sqlalchemy.orm import Session

from app.models.HistoricoClima import Base, InformacaoDiaTemperatura
import urllib

# Connect to the database
odbc_string = os.getenv('stringConnectionAzure')

connect_str = 'mssql+pyodbc:///?odbc_connect=' + urllib.parse.quote_plus(odbc_string)
engine = create_engine(connect_str)
Base.metadata.create_all(engine)

conn = engine.connect()
session = Session(conn)

class InfoRepository:

    def __init__(self):
        self.session = session

    def selectAll(self):
        stmt = select(InformacaoDiaTemperatura)
        return [r.InformacaoDiaTemperatura for r in self.session.execute(stmt)]
    
    def selectByIdDayAndByXdays(self, id_dia, x_dias):
        stmt = select(InformacaoDiaTemperatura).where(InformacaoDiaTemperatura.id_dia == id_dia).where(InformacaoDiaTemperatura.x_dias == x_dias)
        return self.session.execute(stmt).first()
    
    def insertInfo(self, info: InformacaoDiaTemperatura):
        self.session.add(info)    
        return  self.session.commit()

    def updateByIdDay(self):
        pass



