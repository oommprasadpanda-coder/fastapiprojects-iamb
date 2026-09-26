from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def get_apps():
    return {
        "message"  : "message upgraded sucessfully"
    }

