﻿mkdir CSW
cd CSW/
virtualenv .
source bin/activate
pip install django
pip install jsonfield
django-admin.py startproject CSW
cd CSW
mv CSW src
mv CSW CSW2
git clone https://github.com/albertopok/CSW.git
copiar todos los archivos de CSW2 a CSW


Archivo de Git:
git status
echo "db.sqlite3" >> .gitignore
git rm -r --cached src/__pycache__
echo "__pycache__" >> .gitignore
echo "*.pyc" >> .gitignore
git add .gitignore
git commit -m “Commit de inicio”





