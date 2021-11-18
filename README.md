# sem3formal
code for formal languages assigments

# Практика по формальным языкам и трансляциям

Даны α и буква x. Найти максимальное k, такое что в L есть слова, содержащие подслово x^k.

### Подготовка к запуску программы

Перед запуском программы необходимо создать виртуальное окружение:

`python3 -m venv .venv`

Активировать его:

`source .venv/bin/activate`

Установить необходимые библиотеки (для тестирования):

`pip3 install -r requirements.txt`

### Запуск программы

`python3 main.py`

### Запуск тестов

`coverage run -m unittest discover`

Для получения отчёта по code coverage

`coverage report -m`
