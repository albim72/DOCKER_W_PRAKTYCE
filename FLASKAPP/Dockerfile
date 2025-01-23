FROM python:3.11
LABEL authors="Marcin Albiniak"

WORKDIR /app
COPY app.py /app/app.py
RUN pip install flask
EXPOSE 5000
CMD ["python","app.py"]
