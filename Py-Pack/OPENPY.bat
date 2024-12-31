@echo off
color a 
title Open Python Packages/Files

cls

echo Enter name of py file

set /p File="Name: "

py %File%.py