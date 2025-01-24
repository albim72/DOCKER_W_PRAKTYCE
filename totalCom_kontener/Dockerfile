# Użyj obrazu bazowego Windows Server Core
FROM mcr.microsoft.com/windows/servercore:ltsc2022
# Utworzenie katalog roboczy
WORKDIR C:\\TotalCommander

#kopiowanie instalatora Total Commandera do kontenera
COPY ./installer/tcmd1150x64.exe C:\TotalCommander\
# Zainstaluj Total Commander w trybie cichym
RUN C:\TotalCommander\tcmd1150x64.exe /S /D=C:\\TotalCommander

# Ustawienie katalog roboczy
WORKDIR C:\\TotalCommander
# Ustawienie domyślnej komendy (możesz zmodyfikować zgodnie z potrzebami)

CMD ["C:\\TotalCommander\\TOTALCMD64.EXE"]
