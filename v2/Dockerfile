FROM python:3.11-slim

WORKDIR /app

COPY req.txt .

RUN pip install --no-cache-dir -r req.txt

COPY app.py .

EXPOSE 8000

CMD ["python3","app.py"]