currency-converter
=================


### Как запустить проект:


* Клонировать репозиторий:

```
git@github.com:AndrejKazakov/currency-converter.git
```

* В папке с репозиторием создать виртуальное окружение и активировать его:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

* Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

* Выполнить миграции:

```
python3 manage.py migrate
```

* Запустить проект:

```
python3 manage.py runserver
```
