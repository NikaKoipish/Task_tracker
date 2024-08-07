# Task_tracker
# Приложение для отслеживания занятости сотрудников
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)

## Что дает: 
Точное планирование загруженности подчиненных, оперативное перераспределение задач
#
http://localhost:8000/tasks/ - выдает полный список задач.
#
http://localhost:8000/tasks/important/ - запрашивает из БД важные задачи, которые не взяты в работу, но от которых зависят другие задачи, взятые в работу. Осуществляет поиск и выдает список сотрудников, которые могут помочь в выполненинии данной задачи.
#
http://localhost:8000/tasks/employee/active_tasks/ - запрашивает из БД список сотрудников и их задачи, отсортированный по количеству активных задач.

## Технологии:
- python 3.11
- SQL
- django 4.2.2
- PostgreSQL
- DRF
  
## Инструкция по развертыванию:

- Установить зависимости из файла requirements.txt в виртуальное окружение
- Использовать файл env_sample для отражения настроек

## Команда запуска приложения:
- git clone git@github.com:NikaKoipish/Task_tracker.git
- cd Task_tracker
- docker-compose up 

### Автор проекта:
https://github.com/NikaKoipish
