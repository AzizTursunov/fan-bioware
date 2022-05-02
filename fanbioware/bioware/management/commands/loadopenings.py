import os
from csv import DictReader
from django.core.management import BaseCommand
from bioware.models import Opening
from fanbioware.settings import DATA_DIR


class Command(BaseCommand):
    """Загрузка данных в таблицу Opening.
    Можно указать путь к csv-файлу. Если путь не указан,
    загрузка выполняется из DEFAULT_FILE_PATH.
    """

    DEFAULT_FILE_PATH = os.path.join(DATA_DIR, 'openings.csv')
    help = 'Загружает данные из csv-файла в таблицу Opening.'

    def add_arguments(self, parser):
        parser.add_argument(
            'file_path', type=str, nargs='?', default=self.DEFAULT_FILE_PATH
        )

    def handle(self, *args, **options):
        file_path = options['file_path']
        with open(file_path, encoding='utf-8') as csv_file:
            reader = DictReader(csv_file)
            for row in reader:
                _, created = Opening.objects.get_or_create(
                    id=row['id'],
                    studio_id=row['studio_id'],
                    team=row['team'],
                    role=row['role'],
                    description=row['description'],
                    emp_type=row['emp_type'],
                    remote=row['remote'],
                    responsibilities=row['responsibilities'],
                    qualifications=row['qualifications'],
                    perks=row['perks'],
                )
        self.stdout.write(
            self.style.SUCCESS(
                f'Данные из {file_path} успешно загружены.'
            )
        )
