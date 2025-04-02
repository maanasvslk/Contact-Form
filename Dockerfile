
FROM python:3.11.8-slim


WORKDIR /app


LABEL authors="vslkm"


COPY . /app


RUN pip install --no-cache-dir flask


EXPOSE 5000


CMD ["python", "app.py"]