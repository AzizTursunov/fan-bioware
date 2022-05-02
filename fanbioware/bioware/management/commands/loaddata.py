import os
import platform

from django.core.management import BaseCommand
from fanbioware.settings import DATA_DIR


class Command(BaseCommand):
    """ Загружает данные из таблиц в базу данных.

    Файлы с данными должны иметь имена, указанные
    в COMMAND_WITH_CSV_FILE.
    При вызове можно передать путь к папке с csv-файлами.
    Если путь не задан, загрузка выполняется из папки DATA_DIR.
    """

    COMMAND_WITH_CSV_FILE = (
        ('loadgames', 'games.csv'),
        ('loadgameslider', 'gameslider.csv'),
        ('loadnews', 'news.csv'),
        ('loadstudios', 'studios.csv'),
        ('loadstudioslider', 'studioslider.csv'),
        ('loadopenings', 'openings.csv'),
    )
    help = 'Загружает все данные.'

    def add_arguments(self, parser):
        parser.add_argument(
            'file_dir', type=str, nargs='?', default=''
        )

    def handle(self, *args, **options):
        file_dir = options['file_dir']
        for command, csv_file in self.COMMAND_WITH_CSV_FILE:
            if file_dir:
                file_path = os.path.join(file_dir, csv_file)
            else:
                file_path = ''
            if platform.system() == 'Windows':
                os.system(f'python manage.py {command} {file_path}')
            else:
                os.system(f'python3 manage.py {command} {file_path}')
