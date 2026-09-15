Як запустити проект:

Склонуйте репозиторій:
git clone https://github.com/Vlada-sht/web-prog-Shtompil-lab2.git

Створіть та активуйте віртуальне середовище
python -m venv venv
venv\Scripts\activate

Встановіть необхідні бібліотеки
pip install -r requirements.txt

Застосуйте міграції (необхідно для роботи сесій)
python manage.py migrate

Запустіть локальний сервер
python manage.py runserver

Відкрийте сайт
Перейдіть за посиланням в терміналі