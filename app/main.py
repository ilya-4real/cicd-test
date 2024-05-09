from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def greet() -> dict[str, str]:
    return {"message": "hello world"}


@app.get("/cicd_endpoint")
async def new_endpoint():
    return {"message": "this is new endpoint delivered via CICD!! congrats!"}
