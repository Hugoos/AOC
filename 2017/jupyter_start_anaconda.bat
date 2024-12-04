@echo off
CALL "C:\Users\hugoo\anaconda3\Scripts\activate.bat"
CALL activate aoc
pushd %cd%
call jupyter notebook
pause