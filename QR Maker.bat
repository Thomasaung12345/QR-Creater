@echo off 
Title “pip installing”

pip install -r requirements.txt

Title “Launching Python App”
:run
cls
Title “QR Creater Github-Thomasaung12345”
start /b  QR.py
