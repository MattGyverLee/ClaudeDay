FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir flask markdown gunicorn
COPY . .
EXPOSE 5050
CMD ["gunicorn", "--bind", "0.0.0.0:5050", "--workers", "1", "--reload", "app:app"]
