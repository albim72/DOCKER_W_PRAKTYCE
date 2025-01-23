FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir pyramid

EXPOSE 6543

CMD ["python","app.py"]
