FROM python:3.10-slim

WORKDIR /usr/app/

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip setuptools wheel

COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 5000

CMD ["python", "flask_api.py"]