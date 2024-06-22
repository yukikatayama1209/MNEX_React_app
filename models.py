from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class DataTable(Base):
    __tablename__ = 'gasoline_price'

    id = Column(Integer, primary_key=True, index=True)
    SurveyDate = Column(Date, index=True)
    Regular_Hokkaido = Column(Float)
    High_octane_Hokkaido = Column(Float)
    light_oil_Hokkaido = Column(Float)
    Kerosene_Hokkaido = Column(String)
