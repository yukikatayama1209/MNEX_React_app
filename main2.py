from fastapi import FastAPI, Depends, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import DataTable
import plotly.graph_objects as go
import logging

app = FastAPI()

# ログ設定
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# CORSの設定
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# SQLAlchemyセッションの依存性注入
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# WebSocketエンドポイント
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    db: Session = next(get_db())
    try:
        while True:
            data = db.query(DataTable).all()
            data_dict = [{"SurveyDate": row.SurveyDate.strftime("%Y-%m-%d"), "Regular_Hokkaido": row.Regular_Hokkaido} for row in data]
            await websocket.send_text(json.dumps(data_dict))
            await asyncio.sleep(5)  # 5秒ごとにデータを送信
    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        await websocket.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)