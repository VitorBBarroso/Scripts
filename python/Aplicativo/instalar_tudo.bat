@echo off
title Instalador do Renomeador de PDFs
color 0A

echo.
echo Instalando Tesseract OCR...
start /wait tesseract.exe /SILENT

echo.
echo Copiando aplicativo para Program Files...
set "DESTINO=%ProgramFiles%\RenomeadorPDF"
mkdir "%DESTINO%"
copy /Y "Leitor_PDF_3.exe" "%DESTINO%\"

echo.
echo Criando atalho na Área de Trabalho...
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%USERPROFILE%\Desktop\RenomeadorPDF.lnk');$s.TargetPath='%DESTINO%\Leitor_PDF_3.exe';$s.Save()"

echo.
echo Concluído com sucesso!
pause
