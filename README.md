# Конвертер валют

### Описание
converter - это веб-приложение, разработанное на Django, которое позволяет пользователям конвертировать валюты с помощью пользовательского ввода.
Приложение позволяет выбирать валюту, которую нужно конвертировать, а также валюту, в которую нужно конвертировать, а затем выводит результат на экран.

### Установка
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AndrejKazakov/currency-converter.git
```

```
cd currency-converter
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python currency_converter/manage.py migrate
```

Загрузить данные:

```
python currency_converter/manage.py add_data currency
```

Запустить проект:

```
python currency_converter/manage.py runserver
```

### Системные требования
Это приложение написано на языке Python версии 3.8. Для запуска приложения необходимо установить следующие зависимости:

- Django версии 4.2

### Стек технологий
- Python
- Django
- SQLite
