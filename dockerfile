# 使用轻量级 Python 镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 拷贝项目文件
COPY main.py /app
COPY requirements.txt /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 启动 FastAPI 应用
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
