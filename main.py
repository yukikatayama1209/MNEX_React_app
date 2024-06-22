from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, Float, Date
from sqlalchemy.orm import sessionmaker
from fastapi.middleware.cors import CORSMiddleware

from models import DataTable
from database import Base, SessionLocal, engine
import models

"""
DATABASE_URL = "postgresql://postgres:postgres@localhost/mnex"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class DataTable(Base):
    __tablename__ = 'gasoline_price'

    id = Column(Integer, primary_key=True, index=True)
    SurveyDate = Column(Date, index=True)
    Regular_Hokkaido = Column(Float)
    High_octane_Hokkaido = Column(Float)
    light_oil_Hokkaido = Column(Float)
    Kerosene_Hokkaido = Column(String)
"""
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORSの設定
origins = [
    "http://localhost:3000",  # Reactの開発サーバーのURL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/data")
async def read_data(db: Session = Depends(get_db)):
    data = db.query(DataTable).all()
    return data
