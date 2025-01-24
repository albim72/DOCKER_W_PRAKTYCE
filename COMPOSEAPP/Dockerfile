# Użycie oficjalnego obrazu Pythona jako bazowego
FROM python:3.10-slim

# Ustawienie katalogu roboczego w kontenerze
WORKDIR /app

# Skopiowanie lokalnych plików do kontenera
COPY main.py data_processing.py data_struct.py /app/

# Instalacja wymaganych bibliotek
RUN pip install pandas numpy

# Domyślne polecenie (można nadpisać w docker-compose)
CMD ["python", "main.py"]
