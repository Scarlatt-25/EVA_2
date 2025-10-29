FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

CMD ["gunicorn", "agenda_contactos.wsgi:application", "--bind", "0.0.0.0:8080"]