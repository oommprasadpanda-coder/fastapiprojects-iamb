from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message" : "hello from fastapi",
        "message2" : "bitun is a good boy"
    }

