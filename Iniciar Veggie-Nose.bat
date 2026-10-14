@echo off
chcp 65001 >nul
title Veggie-Nose Dashboard
cd /d "%~dp0"

rem 1) Python en el PATH
where python >nul 2>nul
if %errorlevel%==0 (
    python "%~dp0servidor.py"
    goto :eof
)

rem 2) Anaconda del usuario
if exist "%USERPROFILE%\anaconda3\python.exe" (
    "%USERPROFILE%\anaconda3\python.exe" "%~dp0servidor.py"
    goto :eof
)

rem 3) Miniconda del usuario
if exist "%USERPROFILE%\miniconda3\python.exe" (
    "%USERPROFILE%\miniconda3\python.exe" "%~dp0servidor.py"
    goto :eof
)

echo.
echo No se ha encontrado Python en este ordenador.
echo Instala Python (o Anaconda) o usa la version web:
echo   https://ramiro161174.github.io/veggie-nose/
echo.
pause
