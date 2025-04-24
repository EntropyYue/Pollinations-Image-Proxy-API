from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

API_KEY = "pollinations"
BASE_URL = "https://image.pollinations.ai/prompt/"

class ImageRequest(BaseModel):
    prompt: str

@app.post("/v1/images/generations")
async def generate_image(request: Request, payload: ImageRequest):
    # 验证 Authorization 头
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized: Missing Authorization header")
    token = auth_header.split(" ", 1)[1]
    if token != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid API key")

    prompt = payload.prompt.strip()
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt is required")

    image_url = BASE_URL + prompt

    return JSONResponse(
        status_code=200,
        content={
            "created": int(datetime.now().timestamp()),
            "data": [{"url": image_url}]
        }
    )
