# from fastapi import FastAPI

# app = FastAPI()
# @app.get("/")
# def get_apps():
#     return {
#         "message"  : "message upgraded sucessfully"
#     }

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_api():
    return {
        "message"  : "message upgrded sucesffully",
        "error"  : "error not found"
    }