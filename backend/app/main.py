from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from sqlalchemy.sql.sqltypes import Integer, String, Numeric
from sqlalchemy import Table, Column
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy import MetaData

app = FastAPI()

connect_string = "mysql+pymysql://root:RootPassword@mysql:3306/top250_db"

engine = create_engine(connect_string)

meta = MetaData()
connection = engine.connect()

football_transfers = Table(
    'football_transfers', meta,
    Column('Name', String(255), primary_key=True),
    Column('Position', String(255)),
    Column('Age', Integer),
    Column('Team_from', String(255)),
    Column('League_from', String(255)),
    Column('Team_to', String(255)),
    Column('League_to', String(255)),
    Column('Season', String(255)),
    Column('Market_value', String(255)),
    Column('Transfer_fee', Numeric)
)

class Football_transfert(BaseModel):
    Name: str
    Position: str
    Age: int
    Team_from: str
    League_from: str
    Team_to: str
    League_to: str
    Season: str
    Market_value: str
    Transfer_fee: float


@app.get("/Top_250")
async def read_all():
    return connection.execute(football_transfers.select()).fetchall()

@app.get("/{name}")
async def read_by_name(name: str):
    return connection.execute(football_transfers.select().where(football_transfers.c.Name == name)).fetchall()

@app.post("/")
async def write_football_transfert(footballTransfert: Football_transfert):
    connection.execute(football_transfers.insert().values(
        Name = footballTransfert.Name,
        Position = footballTransfert.Position,
        Age = footballTransfert.Age,
        Team_from = footballTransfert.Team_from,
        League_from = footballTransfert.League_from,
        Team_to = footballTransfert.Team_to,
        League_to = footballTransfert.League_to,
        Season = footballTransfert.Season,
        Market_value = footballTransfert.Market_value,
        Transfer_fee = footballTransfert.Transfer_fee
    ))
    return connection.execute(football_transfers.select()).fetchall()

@app.put("/{name}")
async def update_football_transfert(name: str, footballTransfert: Football_transfert):
    connection.execute(football_transfers.update().values(
        Name = footballTransfert.Name,
        Position = footballTransfert.Position,
        Age = footballTransfert.Age,
        Team_from = footballTransfert.Team_from,
        League_from = footballTransfert.League_from,
        Team_to = footballTransfert.Team_to,
        League_to = footballTransfert.League_to,
        Season = footballTransfert.Season,
        Market_value = footballTransfert.Market_value,
        Transfer_fee = footballTransfert.Transfer_fee
    ).where(football_transfers.c.Name == name))
    return connection.execute(football_transfers.select()).fetchall()

@app.delete("/{name}")
async def delete_football_transfert(name: str):
    connection.execute(football_transfers.delete().where(football_transfers.c.Name == name))
    return connection.execute(football_transfers.select()).fetchall()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)