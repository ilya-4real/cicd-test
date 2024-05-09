from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def greet() -> dict[str, str]:
    return {"message": "hello world"}
