echo You need to have python 3.6+ installed and added to your path
echo Creating a virtual environment...
python -m venv venv
echo OK
echo Installing Requirements...
call install_requirements.bat
echo DONE