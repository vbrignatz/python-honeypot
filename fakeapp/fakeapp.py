from fastapi import FastAPI
api = FastAPI()

@api.get('/time')
def get_time():
    return {"data":"00:00:00 01/01/1970"}