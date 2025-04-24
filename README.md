# 🖼️ Pollinations Image Proxy API

A lightweight proxy service compatible with the OpenAI `/v1/images/generations` endpoint. It forwards OpenAI-style image generation requests to [Pollinations](https://image.pollinations.ai).

## 🚀 Features

- ✅ OpenAI-style Compatibility
- 🔐 Requires `Authorization: Bearer pollinations`
- 🐳 Docker & non-Docker ready
- ⚡ Built with FastAPI

## 📦 Project Structure

```
.
├── main.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## 🛠️ Quick Start

### 🔧 Run Without Docker

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 5000
```

### 🐳 Run with Docker

```bash
docker build -t pollinations-api .
docker run -d -p 5000:5000 pollinations-api
```

### 🔑 API Key

All requests must include the following header:

```
Authorization: Bearer pollinations
```

## 📡 API

**POST** `/v1/images/generations`

### Request Body

```json
{
  "prompt": "a futuristic city with flying cars",
  "width": 512,
  "height": 512,
  "model": "flux",
  "enhance": true
}
```

### Parameters

| Name     | Type    | Default | Description |
|----------|---------|---------|-------------|
| prompt   | string  | —       | Text description of the image to generate |
| width    | integer | 512     | Image width in pixels |
| height   | integer | 512     | Image height in pixels |
| model    | string  | flux    | The AI model to employ for image generation (see below) |
| enhance  | boolean | false   | Apply high-resolution enhancement to the generated image |

### Model Options

The `model` field influences both quality and generation style:

- `flux`: General purpose, good quality (default)
- `flux-pro`: General, best quality but slower
- `flux-realism`: Realistically styled images without artistic embellishments
- `flux-anime`: Ideal for anime, manga, and comic styles
- `flux-3d`: Best for intricate 3D-like scenes
- `flux-cablyai`: General purpose with Cablyai inference engine
- `turbo`: Medium to low quality, but marginally faster

Choose a task-specific model if your prompt is closely aligned with one of these styles. Otherwise, `flux` is a solid general-purpose choice.

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.