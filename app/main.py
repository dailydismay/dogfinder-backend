import typing
import datetime
from pydantic import BaseModel
from enum import Enum
from fastapi import FastAPI, Header, status
import uvicorn

app = FastAPI()


class StatusResponse:

  status: str

  def __init__(self, status: str):
    self.status = status  


@app.get('/status')
async def status() -> StatusResponse:
  return StatusResponse('up')


@app.get('/square/{digit}')
async def square(digit: int) -> int:
  return digit ** 2


@app.get('/mul')
async def mul(x: int, y: int = 0) -> int:
  return x * y


class LogLevel(str, Enum):
  info: str = "info"
  warn: str = "warn"
  err: str = "err"


class Log(BaseModel):
  msg: str
  level: LogLevel = LogLevel.info


@app.post('/log', status_code=status.HTTP_201_CREATED)
async def log(log_data: Log) -> Log:
  print(f"\t\t- [{log_data.level}] {log_data.msg}")
  return {'created_at': datetime.datetime.now(), **log_data.dict()}


if __name__ == "__main__":
  uvicorn.run("main:app", host="127.0.0.1", port=5500,
              log_level="info")
