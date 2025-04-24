from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime
from urllib.parse import quote

app = FastAPI()

API_KEY = "pollinations"
BASE_URL = "https://image.pollinations.ai/prompt/"

class ImageRequest(BaseModel):
    prompt: str
    width: int = 512
    height: int = 512
    model: str = "stable-diffusion"
    enhance: bool = False

@app.post("/v1/images/generations")
async def generate_image(request: Request, payload: ImageRequest):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized: Missing Authorization header")
    token = auth_header.split(" ", 1)[1]
    if token != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid API key")

    prompt = payload.prompt.strip()
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt is required")

    image_url = (
        f"{BASE_URL}{quote(prompt)}"
        f"?width={payload.width}&height={payload.height}"
        f"&model={payload.model}&nologo=true&enhance={str(payload.enhance).lower()}"
    )

    return JSONResponse(
        status_code=200,
        content={
            "created": int(datetime.now().timestamp()),
            "data": [{"url": image_url}]
        }
    )
