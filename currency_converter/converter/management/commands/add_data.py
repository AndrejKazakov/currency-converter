import csv
import os
from django.core.management.base import BaseCommand
from converter.models import Currency


class Command(BaseCommand):
    """
    Добавляет данные из csv файлов в модели.
    Для запуска скрипта: python currency_converter/manage.py add_data [модель]
    """

    def add_arguments(self, parser):
        parser.add_argument('model', type=str, help='model')

    def handle(self, *args, **options):
        dir_path = os.path.abspath(
            os.path.join('.', 'currency_converter', 'static', 'data')
        )

        file_model = {
            'currency': {'currency.csv': Currency},
        }

        if options['model'].lower() in file_model:
            obj = file_model[options['model'].lower()]
            file, model = list(item for item in obj.items())[0]
            path = os.path.join(dir_path, file)

            obj_list = []
            with open(path, encoding='cp1251') as csv_file:
                for obj_dict in csv.DictReader(csv_file):
                    obj_list.append(model(**obj_dict))
                model.objects.bulk_create(obj_list)
        else:
            raise Exception('Такой модели нет')
