FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY tests/run_tests.py /app/run_tests.py

CMD ["python", "app.py"]
