from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import DataTable
import plotly.graph_objects as go
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# フロントエンドとのCORSを許可
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React開発サーバーのURL
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

def get_plot_data(db: Session):
    data = db.query(DataTable).all()
    
    # デバッグ：取得したデータを確認する
    print(data)
    
    # グラフの作成（ここでは例として折れ線グラフを作成）
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[row.SurveyDate for row in data],
                             y=[row.Regular_Hokkaido for row in data],
                             mode='lines',
                             name='Regular Hokkaido'))
    fig.update_layout(title='Regular Hokkaido Prices Over Time')
    
    return fig

# データを取得してJSONレスポンスを返すエンドポイント
@app.get("/data", response_class=JSONResponse)
async def read_data(db: Session = Depends(get_db)):
    data = db.query(DataTable).all()
    data_dict = [
        {
            "SurveyDate": row.SurveyDate,
            "Regular_Hokkaido": row.Regular_Hokkaido,
            "High_octane_Hokkaido": row.High_octane_Hokkaido,
            "light_oil_Hokkaido": row.light_oil_Hokkaido,
            "Kerosene_Hokkaido": row.Kerosene_Hokkaido
        } for row in data
    ]
    return data_dict

# グラフを表示するエンドポイント
@app.get("/plot", response_class=JSONResponse)
async def plot_data(db: Session = Depends(get_db)):
    fig = get_plot_data(db)
    plot_html = fig.to_html(full_html=False, default_height=500, default_width=700)
    return {"plot_html": plot_html}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
