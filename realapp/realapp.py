from datetime import datetime

from fastapi import FastAPI
api = FastAPI()

@api.get('/time')
def get_time():
    return {'data':datetime.now().strftime("%H:%M:%S %d/%m/%Y")}