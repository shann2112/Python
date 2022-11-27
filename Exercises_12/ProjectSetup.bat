@echo off
cls
echo "**********************************************"
echo
echo This batch file will create a project directory
echo Michaael Shannon L00177543 21/10/2022
echo
echo "**********************************************"
echo *** press [ctrl][c] to exit or any key to continue ***
pause
set /p NAME=Enter the name of the project, then press [return]
echo Creating %NAME%
mkdir %NAME%
cd %NAME%
mkdir Documentation
mkdir Tests
mkdir Examples
mkdir Source
cls
dir
echo "**********************************************"
echo Finished creating project %NAME%
echo "**********************************************"
cd ..