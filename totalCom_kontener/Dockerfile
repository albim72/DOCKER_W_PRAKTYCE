# Użyj obrazu bazowego Windows Server Core
FROM mcr.microsoft.com/windows/servercore:ltsc2022
# Ustaw katalog roboczy
WORKDIR C:\\TotalCommander
# Pobierz instalator Total Commandera (wersja demo)
ADD https://ghisler.com/amazons3.php?d=tcmd1050x64.exe tcmd_installer.exe
# Zainstaluj Total Commander w trybie cichym
RUN tcmd_installer.exe /S /D=C:\\TotalCommander
# Ustawienie domyślnej komendy (możesz zmodyfikować zgodnie z potrzebami)
CMD ["C:\\TotalCommander\\TOTALCMD64.EXE"]