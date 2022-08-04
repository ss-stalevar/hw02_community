# Сообщества

[![CI](https://github.com/yandex-praktikum/hw02_community/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/yandex-praktikum/hw02_community/actions/workflows/python-app.yml)
[![Python](https://img.shields.io/badge/-Python-464641?style=flat-square&logo=Python)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/-pytest-464646?style=flat-square&logo=pytest)](https://docs.pytest.org/en/6.2.x/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![HTML5](https://img.shields.io/badge/-HTML5-464646?style=flat-square&logo=html5)](https://en.wikipedia.org/wiki/HTML5)
[![CSS](https://img.shields.io/badge/-CSS-464646?style=flat-square&logo=css3)](https://en.wikipedia.org/wiki/CSS)

Яндекс Практикум. Спринт 3. Итоговый проект.

## Описание

Приложение ```Posts``` отображает десять последних записей сообществ на главной странице сайта. Можно перейти на страницу отдельного сообщества, где отображаются десять последних публикаций этой группы.

## Функционал

* Создано и зарегистрировано приложение Posts;
* Подключена база данных;
* Десять последних записей выводятся на главную страницу;
* В админ-зоне доступно управление объектами модели ```Post```. Можно публиковать новые записи, редактировать и удалять существующие;
* Пользователь может перейти на страницу любого сообщества, где отображаются десять последних публикаций из этой группы.

## Установка

Клонировать репозиторий:

```python
git clone https://github.com/egorcoders/hw02_community.git
```

Перейти в папку с проектом:

```python
cd hw02_community/
```

Установить виртуальное окружение для проекта:

```python
python -m venv venv
```

Активировать виртуальное окружение для проекта:

```python
# для OS Lunix и MacOS
source venv/bin/activate

# для OS Windows
source venv/Scripts/activate
```

Установить зависимости:

```python
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции на уровне проекта:

```python
cd yatube
python3 manage.py makemigrations
python3 manage.py migrate
```

Запустить проект локально:

```python
python3 manage.py runserver

# адрес запущенного проекта
http://127.0.0.1:8000
```

Зарегистирировать суперпользователя Django:

```python
python3 manage.py createsuperuser

# адрес панели администратора
http://127.0.0.1:8000/admin
```
