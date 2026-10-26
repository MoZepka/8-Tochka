from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

response_body = [
  {
    "id": 1,
    "name": "Международная космическая станция",
    "orbit": "Низкая околоземная орбита (НОО)",
    "crew": 7
  },
  {
    "id": 2,
    "name": "Lunar Gateway",
    "orbit": "Окололунная гало-орбита",
    "crew": 4
  },
  {
    "id": 3,
    "name": "Марсианский орбитальный комплекс",
    "orbit": "Ареоцентрическая орбита",
    "crew": 0
  }
]

class StationsCreate(BaseModel):
    name: str
    orbit: str
    crew: int

class Stations(BaseModel):
    id: int
    name: str
    orbit: str
    crew: int

@app.get("/stations", response_model=list[Stations])
def stations_get():
    return response_body

@app.post("/stations", response_model=Stations, status_code=201)
def station_post(station: StationsCreate):
    new_station = station.model_dump()
    new_station["id"] = len(response_body) + 1
    response_body.append(new_station)
    return new_station

