from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

handler = Mangum(app)  # Mangum is used to adapt FastAPI for Lambda
