# 🖼️ Pollinations Image Proxy API

A lightweight proxy service compatible with the OpenAI `/v1/images/generations` endpoint. It forwards OpenAI-style image generation requests to [Pollinations](https://image.pollinations.ai), ideal for local deployment and microservice architecture.

## 🚀 Features

- ✅ **OpenAI-style Compatibility**: Accepts `prompt` request body format.
- 🔐 **API Key Protection**: Requires `Authorization: Bearer pollinations` header.
- 🐳 **Docker Ready**: Lightweight image for microservice deployment.
- ⚡ **Built with FastAPI**: High performance with automatic OpenAPI documentation.

## 📦 Project Structure

```
.
├── main.py             # FastAPI app entry
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker build file
└── README.md           # Project documentation
```

## 🛠️ Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/yourname/pollinations-api-proxy.git
cd pollinations-api-proxy
```

### 2. Build Docker image

```bash
docker build -t pollinations-api .
```

### 3. Run the container

```bash
docker run -d -p 5000:5000 pollinations-api
```

## 📡 API Endpoint

### POST `/v1/images/generations`

**Headers:**
```
Authorization: Bearer pollinations
Content-Type: application/json
```

**Request Body:**
```json
{
  "prompt": "a futuristic city with flying cars"
}
```

**Response Body:**
```json
{
  "created": 1713945600,
  "data": [
    {
      "url": "https://image.pollinations.ai/prompt/a futuristic city with flying cars"
    }
  ]
}
```

## 🧪 Example Request

```bash
curl -X POST http://localhost:5000/v1/images/generations   -H "Authorization: Bearer pollinations"   -H "Content-Type: application/json"   -d '{"prompt": "a robot playing violin in a concert hall"}'
```

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
