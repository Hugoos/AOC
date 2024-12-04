@echo off
CALL "C:\Users\husp\Anaconda3\Scripts\activate.bat"
CALL activate routing
pushd %cd%
call jupyter notebook
pause