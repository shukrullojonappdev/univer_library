# Библиотека

### Настройка виртуального окружение

> Эти команды предназначены для системы Windows

Создайте venv

```console
py -m venv .\app\venv
```

Активируйте venv

```console
.\app\venv\Scripts\activate
```

Установите необходимые пакеты

```console
pip install -r .\app\requirement.txt
```

Что бы работать с manage.py с начала поменяйте директиву

```console
cd .\app\api\
```

Запуск сервера

```console
py .\manage.py runserver
```

### Во время разработки что бы обновить стили нажмите в браузере
> Ctrl + F5